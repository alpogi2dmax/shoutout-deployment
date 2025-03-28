#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, send_from_directory
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User


# Views go here!

# def serve():
#        return send_from_directory(app.static_folder, 'index.html')

# @app.route('/<path:path>')
# def static_proxy(path):
#     return send_from_directory(app.static_folder, path)


@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    # app.run(port=5555, debug=True)
    app.run()

