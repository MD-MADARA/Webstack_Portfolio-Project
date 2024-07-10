#!/usr/bin/python3
from flask import render_template
from routes.__init__ import view_blueprint
import uuid


@view_blueprint.route('/men', strict_slashes=False)
def men_page():
    """product route"""
    return render_template('men.html', cache_id=uuid.uuid4())
