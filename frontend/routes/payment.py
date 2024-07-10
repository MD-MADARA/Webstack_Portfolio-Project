#!/usr/bin/python3
from flask import render_template
from routes.__init__ import view_blueprint
import uuid


@view_blueprint.route('/payment', strict_slashes=False)
def payment():
    """payment  route"""
    return render_template('payment.html', cache_id=uuid.uuid4())
