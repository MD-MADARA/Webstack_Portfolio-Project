#!/usr/bin/python3
""" Api module """
from flask import Flask, make_response, jsonify
from backend import storage
from backend.api.views import app_views
from flasgger import Swagger
import yaml


app = Flask(__name__)
app.register_blueprint(app_views)

# Load YAML schema files
user_schema = yaml.safe_load(open('backend/api/docs/models/user_schema.yml'))
cart_schema = yaml.safe_load(open('backend/api/docs/models/cart_schema.yml'))
order_schema = yaml.safe_load(open('backend/api/docs/models/order_schema.yml'))
order_item_schema = yaml.safe_load(open('backend/api/docs/models/order_item_schema.yml'))
product_schema = yaml.safe_load(open('backend/api/docs/models/product_schema.yml'))
shared_base_schema = yaml.safe_load(open('backend/api/docs/models/shared_base_schema.yml'))

swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Your API",
        "description": "API documentation",
        "version": "1.0.0"
    },
    "definitions": {
        "User": user_schema['User'],
        "Cart": cart_schema['Cart'],
        "Order": order_schema['Order'],
        "OrderItem": order_item_schema['OrderItem'],
        "Product": product_schema['Product'],
        "SharedBase": shared_base_schema['SharedBase']
    }
})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(_):
    """
    404 Error
    ---
    """
    return make_response(jsonify({'error': "Not Found"}), 404)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5001, threaded=True)
