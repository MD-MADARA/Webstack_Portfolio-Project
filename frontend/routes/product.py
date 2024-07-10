#!/usr/bin/python3
from flask import render_template
from routes.__init__ import view_blueprint
import uuid

@view_blueprint.route('/product/<int:id>', strict_slashes=False)
def prduct(id):
    """product route"""
    return render_template('product.html', cache_id=uuid.uuid4())
