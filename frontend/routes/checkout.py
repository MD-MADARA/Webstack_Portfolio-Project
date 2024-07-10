from flask import render_template
from routes.__init__ import view_blueprint
import uuid

@view_blueprint.route('/checkout', strict_slashes=False)
def checkout():
    """checkout page"""
    return render_template('checkout.html', cache_id=uuid.uuid4())
