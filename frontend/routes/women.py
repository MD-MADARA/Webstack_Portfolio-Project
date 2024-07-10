#!/usr/bin/python3
from flask import render_template
from routes.__init__ import view_blueprint
import uuid

@view_blueprint.route('/women', strict_slashes=False)
def women_page():
    """product route"""
    return render_template('women.html', cache_id=uuid.uuid4())
