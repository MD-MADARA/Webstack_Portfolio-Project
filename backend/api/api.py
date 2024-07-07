#!/usr/bin/python3
""" Api module """
from flask import Flask, make_response, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'], strict_slashes=False)
def test():
    """ test the api
    """
    return jsonify({'message': 'hello world'})

@app.errorhandler(404)
def not_found(_):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not Found"}), 404)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5001, threaded=True)
