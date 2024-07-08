#!/usr/bin/python3
""" User view """
from backend import storage
from backend.data_models.product import Product
from backend.api.views import app_views
from backend.logging_config import logger 
from flask import jsonify, abort, make_response, request
from flasgger import swag_from

def get_product_by_id(id):
    """get product by id"""
    product = storage.get_by_id(Product, id)
    if not product:
        logger.warning(f"Product with ID {id} not found")
        abort(404, description="Product not found")
    return product

@app_views.route('/products', methods=['GET'], strict_slashes=False)
@swag_from('../docs/product/get_products.yml')
def get_products():
    """
    Retrieves the list of all products
    or a specific product.
    """
    category_name = request.args.get('category_name')
    category_type = request.args.get('category_type')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    limit = request.args.get('limit')
    order_asc = request.args.get('asc_order_by')
    order_desc = request.args.get('desc_order_by')
    start_from = request.args.get('from')
    ignore = request.args.get('ignore')

    # Build filter dictionary
    filter = {}
    if category_type:
        filter['category_type'] = category_type
    if category_name:
        filter['category_name'] = category_name
    if min_price:
        filter['price'] = lambda p: p >= float(min_price)
    if max_price:
        filter['price'] = lambda p: p <= float(max_price)

    # Fetch products from storage
    products = storage.all(Product, order_asc=order_asc, order_desc=order_desc, filter=filter).values()
    filtered_products = [pd.dict_format() for pd in products]

    # Apply filters that cannot be applied directly in the query
    if ignore and ignore.isdigit():
        ignore = int(ignore)
        filtered_products = [p for p in filtered_products if p['id'] != ignore]

    if start_from and start_from.isdigit():
        start_from = int(start_from)
        filtered_products = filtered_products[start_from:]

    # Limit the number of products if 'limit' parameter is provided
    if limit and limit.isdigit():
        limit = int(limit)
        filtered_products = filtered_products[:limit]

    return make_response(jsonify(filtered_products), 200)


@app_views.route('/products/<str:id>', methods=['GET'], strict_slashes=False)
@swag_from('../docs/product/get_product.yml')
def get_product(id):
    """
    Retrieves a product by its ID.
    """
    product = get_product_by_id(id)
    return make_response(jsonify(product.dict_format()), 200)


@app_views.route('/products/<str:id>', methods=['DELETE'], strict_slashes=False)
@swag_from('../docs/product/delete_product.yml')
def delete_product(id):
    """
    Deletes a product by its ID.
    """
    product = get_product_by_id(id)

    product.delete()
    storage.save()
    return make_response(jsonify({"message": "Product deleted successfully"}), 200)


@app_views.route('/products', methods=['POST'], strict_slashes=False)
@swag_from('../docs/product/post_product.yml')
def post_product():
    """
    Creates a new product.
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    required_fields = ['title', 'price', 'description', 'category_name', 'category_type', 'image_url']

    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing {field}")

    instance = Product(**data)
    instance.save()
    return make_response(jsonify(instance.dict_format()), 201)


@app_views.route('/products/<str:id>', methods=['PUT'], strict_slashes=False)
@swag_from('../docs/product/put_product.yml')
def put_product(id):
    """
    Updates a product by its ID.
    udpate password is not implemented yet
    """
    product = get_product_by_id(id)

    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()

    ignore = ['id', 'created_date', 'updated_date', 'product_code']

    for key, value in data.items():
        if key not in ignore and hasattr(product, key):
            setattr(product, key, value)

    product.save()
    return make_response(jsonify(product.dict_format()), 200)
