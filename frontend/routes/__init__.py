from flask import Blueprint

view_blueprint = Blueprint('view_blueprint', __name__)

from routes.product import *
from routes.signup import *
from routes.profile import *
from routes.men import *
from routes.women import *
from routes.about import *
from routes.checkout import *
from routes.payment import *
