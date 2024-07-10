from flask import render_template
from routes.__init__ import view_blueprint
import uuid

@view_blueprint.route('/about', strict_slashes=False)
def about():
    """about page"""
    return render_template('aboutus.html', cache_id=uuid.uuid4())
