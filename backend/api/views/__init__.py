#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api')

# Import routes to register them with the blueprint
from backend.api.views.api_status import *
from backend.api.views.user_view import *
from backend.api.views.product_view import *
from backend.api.views.cart_view import *
from backend.api.views.order_view import *
