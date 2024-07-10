#!/usr/bin/python3
from flask import render_template
from routes.__init__ import view_blueprint
import uuid

@view_blueprint.route('/profile', strict_slashes=False)
def profile():
    """profile route"""
    return render_template('profile.html', cache_id=uuid.uuid4())
