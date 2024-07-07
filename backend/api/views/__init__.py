#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api')

from backend.api.views.api_status_view import *
# from backend.api.views.user_view import *
# from backend.api.views.product_view import *
# from backend.api.views.order_view import *
# from backend.api.views.order_items_view import *
# from backend.api.views.login_view import *
# from backend.api.views.cart_view import *
