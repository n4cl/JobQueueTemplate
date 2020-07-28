import os
from flask import Flask, render_template
import json

def create_app():
    app = Flask(__name__)

    @app.route("/hello")
    def hello():
        return json.dumps({'message': "Hello World"}), 200

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
