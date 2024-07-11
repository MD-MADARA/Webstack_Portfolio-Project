#!/usr/bin/python3
""" User view """
from backend.api.views.__init__ import app_views
from flask import jsonify, make_response
from backend import storage
from backend.models.product import Product
from backend.models.user import User
from backend.models.order import Order


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return make_response(jsonify({"status": "OK"}), 200)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def objects_stats():
    """ Retrieves the number of each objects by type """
    classes = {
        "Product": Product, "User": User, "Order": Order
    }

    stats = {}
    for key, value in classes.items():
        stats[key] = storage.count(value)

    return make_response(jsonify(stats), 200)
