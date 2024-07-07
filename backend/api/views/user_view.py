#!/usr/bin/python3
""" User view """
from backend import storage
from backend.data_models.user import User
from backend.data_models.cart import Cart
from backend.api.views.__init__ import app_views
from flask import jsonify, abort, make_response, request



@app_views.route('/users/<int:id>', methods=['GET'], strict_slashes=False)
def get_user(id):
    """get user by id"""
    user = storage.get_by_id(User, id)
    if not user:
        abort(404)
    return make_response(jsonify(user.dict_format()), 200)



@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrieves the list of all user objects
    """
    limit = request.args.get('limit')
    email = request.args.get('email')
    if email:
        user = storage.get_user_by_email(email)
        if not user:
            abort(404)
        return jsonify(user.to_dict())

    users = [user.to_dict() for user in storage.all(User).values()]
    filtered_users = users
    if limit:
        limit = int(limit)
        filtered_users = filtered_users[:limit]
    return jsonify(filtered_users)
