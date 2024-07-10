#!/usr/bin/python3
from flask import Flask, render_template
from routes.__init__ import view_blueprint
import uuid

app = Flask(__name__)
app.register_blueprint(view_blueprint)
app.url_map.strict_slashes = False

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", cache_id=uuid.uuid4())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
