#!/usr/bin/python3
""" Cart view """
from backend import storage
from backend.models.cart import Cart
from backend.models.cart_item import CartItem
from backend.models.product import Product
from backend.models.user import User
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


def get_from_data(data, field):
    """get field from data"""
    if field not in data:
        abort(400, description=f"Missing {field}")
    return data.get(field)

def verify_product_id(id):
    """verify productID"""
    product = storage.get_by_id(Product, id)
    if not product:
        logger.warning(f"Invalid productId")
        abort(400, description="Invalid productId")
    return id

def verify_quantity(quantity):
    """verify quantity"""
    if type(quantity) != int:
        abort(400, description="quantity value must be an integer")
    return quantity


def validate_add_to_cart_data(data):
    """validate and return required data fields"""
    product_id = verify_product_id(get_from_data(data, 'product_id'))
    quantity = verify_quantity(get_from_data(data, 'quantity'))
    return product_id, quantity

def validate_delete_from_cart_data(data):
    """validate and return required data fields"""
    return verify_product_id(get_from_data(data, 'product_id'))

def validate_update_item_data(data):
    """validate and return required data fields"""
    return verify_quantity(get_from_data(data, 'quantity'))

# GET api/users/{user_id}/cart
@app_views.route('/users/<string:user_id>/cart', methods=['GET'], strict_slashes=False)
#@swag_from('../docs/cart/get_cart.yml')
def get_cart(user_id):
    """Get cart by userID"""
    user = get_user_by_id(user_id)
    cart = user.cart.dict_format()
    cart_items_list = user.cart.cart_items
    items = {
        "cart_items": [item.dict_format() for item in cart_items_list]
    }
    apiResponse = {**cart, **items}
    return make_response(jsonify(apiResponse), 200)

# POST api/users/{user_id}/cart/products
@app_views.route('/users/<string:user_id>/cart/products', methods=['POST'], strict_slashes=False)
#@swag_from('../docs/user/post_user.yml')
def add_to_cart(user_id):
    """Add product to cart"""
    user = get_user_by_id(user_id)
    cart = user.cart
    cart_id = cart.id
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    (productId, quantity) = validate_add_to_cart_data(data)

    # check if product already exists in cart
    foundInCart = False
    for item in cart.cart_items:
        if item.product_id == productId:
            # if item already in cart increase it's quantity
            foundInCart = True
            item.quantity += quantity
            break

    if not foundInCart:
        cartItem = CartItem(cart_id=cart_id, **data)
        cartItem.save()


    # save updates
    cart.save()
    items = {
        "cart_items": [item.dict_format() for item in cart.cart_items]
    }
    apiResponse = {
        "message": f"Product with ID {productId} added to cart successfully",
        "cart": {**cart.dict_format(), **items}
    }
    return make_response(jsonify(apiResponse), 201)

# DELETE api/users/{user_id}/cart/products
@app_views.route('/users/<string:user_id>/cart/products', methods=['DELETE'], strict_slashes=False)
#@swag_from('../docs/user/delete_user.yml')
def delete_from_cart(user_id):
    """delete product from cart"""

    user = get_user_by_id(user_id)
    cart = user.cart

    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    productId = validate_delete_from_cart_data(data)

    foundInCart = False
    for item in cart.cart_items:
        if item.product_id == productId:
            foundInCart = True
            # remove item from cart when found
            item.delete()
            cart.save()
            break

    if not foundInCart:
        logger.warning(f"Product with ID {productId} not found in cart")
        abort(404, description="Product not found in cart")

    items = {
        "cart_items": [item.dict_format() for item in cart.cart_items]
    }
    apiResponse = {
        "message": f"Product with ID {productId} removed from cart successfully",
        "cart": {**cart.dict_format(), **items}
    }
    return make_response(jsonify(apiResponse), 200)

# PATCH api/users/{user_id}/cart/products/{product_id}
@app_views.route('/users/<string:user_id>/cart/products/<string:product_id>', methods=['PATCH'], strict_slashes=False)
#@swag_from('../docs/user/delete_user.yml')
def update_in_cart(user_id, product_id):
    """update item of cart"""
    user = get_user_by_id(user_id)
    cart = user.cart
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    productId = validate_update_item_data(data)

    foundInCart = False
    for item in cart.cart_items:
        if item.product_id == productId:
            foundInCart = True
            # remove item from cart when found
            item.delete()
            cart.save()
            break

    if not foundInCart:
        logger.warning(f"Product with ID {productId} not found in cart")
        abort(404, description="Product not found in cart")

    items = {
        "cart_items": [item.dict_format() for item in cart.cart_items]
    }
    apiResponse = {
        "message": f"Product with ID {productId} removed from cart successfully",
        "cart": {**cart.dict_format(), **items}
    }
    return make_response(jsonify(apiResponse), 200)
