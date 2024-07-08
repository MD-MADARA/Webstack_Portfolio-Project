#!/usr/bin/python3
""" Api module """
from flask import Flask, make_response, jsonify
from backend.api.views.__init__ import app_views
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(app_views)
swagger = Swagger(app)


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
