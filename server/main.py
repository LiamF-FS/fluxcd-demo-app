from flask import Flask
from flask_cors import CORS
from random import randrange

def create_app():

    app = Flask(__name__)

    origins = "*"

    CORS(app, resources={r"*": {"origins": origins}})

    @app.route('/spin-foundry')
    def lets_spin():

        return { 'spins': randrange(10) }, 200

    return app
