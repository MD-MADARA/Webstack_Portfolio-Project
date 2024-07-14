#!/usr/bin/python3
""" Oder view """
from backend import storage
from backend.models.order import Order
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

def order_items_to_dict(item):
    dictionnary = item.dict_format()
    del dictionnary['cart_id']
    return dictionnary


def get_from_data(data, field):
    """get field from data"""
    if field not in data:
        abort(400, description=f"Missing {field}")
    return data.get(field)

def verify_total_price(total):
    """verify total price """
    if type(total) != float:
        abort(400, description="total price value must be a float number")
    if float(total) < 0:
        abort(400, description="Invalid price")
    return total


# GET api/users/{user_id}/orders
# GET api/users/orders
@app_views.route('/users/<string:user_id>/orders', methods=['GET'], strict_slashes=False)
@app_views.route('/users/orders', methods=['GET'], strict_slashes=False)
@swag_from('../docs/orders/get_orders.yml')
def get_orders(user_id=None):
    """Get orders"""
    if user_id:
        user = get_user_by_id(user_id)
        all_orders = user.orders
    else:
        all_orders = storage.all(Order).values()

    apiResponse = []
    for o in all_orders:
        order = o.dict_format()
        order_items_list = o.items
        items = {
            "order_items": [order_items_to_dict(item) for item in order_items_list]
        }
        apiResponse.append({**order, **items})
    
    return make_response(jsonify(apiResponse), 200)




# POST api/users/{user_id}/orders
@app_views.route('/users/<string:user_id>/orders', methods=['POST'], strict_slashes=False)
@swag_from('../docs/orders/post_order.yml')
def add_order(user_id):
    """Add product to cart"""
    user = get_user_by_id(user_id)

    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    totalPrice = verify_total_price(get_from_data(data, 'total_price'))

    # create empty order
    new_order = Order(user_id=user.id, total_price=totalPrice)
    new_order.save()
    # move all cart items from cart to the order
    cart = user.cart
    for item in cart.cart_items:
        item.order_id = new_order.id
        item.cart_id = None
        item.save()

    # save changes
    cart.save()
    new_order.save()

    order = new_order.dict_format()
    order_items_list = new_order.items
    items = {
        "order_items": [order_items_to_dict(item) for item in order_items_list]
    }

    apiResponse = {
        "message": f"Order with ID {new_order.id} created successfully",
        "order": {**order, **items}
    }

    return make_response(jsonify(apiResponse), 201)
