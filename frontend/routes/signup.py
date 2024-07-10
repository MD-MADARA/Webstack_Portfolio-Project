#!/usr/bin/python3
from flask import render_template
from routes.__init__ import view_blueprint
import uuid


@view_blueprint.route('/signup', strict_slashes=False)
def sign_up():
    """product route"""
    return render_template('signup.html', cache_id=uuid.uuid4())


@view_blueprint.route('/login', strict_slashes=False)
def log_in():
    """product route"""
    return render_template('login.html', cache_id=uuid.uuid4())
