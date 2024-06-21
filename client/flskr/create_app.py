from flask import Flask
import secrets

def create_app():
    app = Flask(__name__)
    secret = secrets.token_hex(32)
    app.config['SECRET_KEY'] = secret
    return app