#!/usr/bin/python3
""" User view """
from backend import storage
from backend.data_models.user import User
from backend.data_models.cart import Cart
from backend.api.views import app_views
from backend.logging_config import logger 
from flask import jsonify, abort, make_response, request
from flasgger import swag_from
import re


# Regular expression for password validation
# (at least 8 characters, one uppercase, one lowercase, one digit, 
# and one special character)
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
# Regular expression for basic email format validation
EMAIL_REGEX = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'

def get_user_by_id(id):
    """get user by id"""
    user = storage.get_by_id(User, id)
    if not user:
        logger.warning(f"User with ID {id} not found")
        abort(404, description="User not found")
    return user

def validate_user_data(data):
    """validate request data"""
    required_fields = ['email', 'password', 'first_name', 'last_name', 'address', 'phone']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing {field}")
    
    # Validate email format using regex
    if not re.match(EMAIL_REGEX, data.get('email')):
        abort(400, description="Invalid email format")

    if not re.match(PASSWORD_REGEX, data.get('password')):
        abort(400, description="Password must meet specified requirements")

    if storage.get_user_by_email(data.get("email")):
        abort(400, description="Email already exists")


# GET api/users/{id}
@app_views.route('/users/<str:id>', methods=['GET'], strict_slashes=False)
@swag_from('../docs/user/get_user.yml')
def get_user(id):
    """Get user by ID"""
    user = get_user_by_id(id)
    return make_response(jsonify(user.dict_format()), 200)

# GET api/users
@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('../docs/user/get_users.yml')
def get_users():
    """Retrieves the list of all user objects"""
    limit = request.args.get('limit')
    email = request.args.get('email')
    if email:
        user = storage.get_user_by_email(email)
        if not user:
            abort(404, description="User not found")
        return make_response(jsonify(user.dict_format()), 200)

    users = [user.dict_format() for user in storage.all(User).values()]
    if limit:
        limit = int(limit)
        users = users[:limit]
    return make_response(jsonify(users), 200)


# DELETE api/users/{id}
@app_views.route('/users/<str:id>', methods=['DELETE'], strict_slashes=False)
@swag_from('../docs/user/delete_user.yml')
def delete_user(id):
    """Deletes a user object"""
    user = get_user_by_id(id)
    user.delete()
    storage.save()
    return make_response(jsonify({"message": "User deleted successfully"}), 200)


# POST api/users
@app_views.route('/users', methods=['POST'], strict_slashes=False)
@swag_from('../docs/user/post_user.yml')
def post_user():
    """Creates a user"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    validate_user_data(data)

    user = User(**data)
    user.save()
    cart = Cart(user_id=user.id)
    cart.save()
    user.cart_id = cart.id
    user.save()
    return make_response(jsonify({"message": "successfully registered"}), 201)


# PUT api/users/{id}
@app_views.route('/users/<str:id>', methods=['PUT'], strict_slashes=False)
@swag_from('../docs/user/put_user.yml')
def put_user(id):
    """Updates a user"""
    user = get_user_by_id(id)
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'created_date', 'updated_date']
    data = request.get_json()
    password = data.get('password', None)
    if password and not re.match(PASSWORD_REGEX, password):
        abort(400, description="Password must meet specified requirements")

    for key, value in data.items():
        if key not in ignore and hasattr(user, key):
            setattr(user, key, value)
    user.save()
    return make_response(jsonify({"message": "User updated successfully"}), 200)
