#!/usr/bin/python3
""" User view """
from backend import storage
from backend.data_models.user import User
from backend.data_models.cart import Cart
from backend.api.views import app_views
from backend.logging_config import logger 
from flask import jsonify, abort, make_response, request
from flasgger import swag_from



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
    if len(data.get("password", "")) < 8:
        abort(400, description="Password must be at least 8 characters long")
    if storage.get_user_by_email(data.get("email")):
        abort(400, description="Email already exists")


# GET api/users/{id}
@swag_from('../docs/get_user.yml')
@app_views.route('/users/<int:id>', methods=['GET'], strict_slashes=False)
def get_user(id):
    """Get user by ID"""
    user = get_user_by_id(id)
    return make_response(jsonify(user.dict_format()), 200)

# GET api/users
@swag_from('../docs/get_users.yml')
@app_views.route('/users', methods=['GET'], strict_slashes=False)
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
@swag_from('../docs/delete_user.yml')
@app_views.route('/users/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_user(id):
    """Deletes a user object"""
    user = get_user_by_id(id)
    user.delete()
    storage.save()
    return make_response(jsonify({}), 200)


# POST api/users
@swag_from('../docs/post_user.yml')
@app_views.route('/users', methods=['POST'], strict_slashes=False)
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
    return make_response(jsonify({"description": "successfully registered"}), 201)


# PUT api/users/{id}
@swag_from('../docs/put_user.yml')
@app_views.route('/users/<int:user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """Updates a user"""
    user = get_user_by_id(user_id)
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore and hasattr(user, key):
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.dict_format()), 200)
