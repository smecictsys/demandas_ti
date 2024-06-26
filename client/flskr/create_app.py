from flask import Flask
import secrets
from .modules.ti.ti import bp_ti
from .modules.usuarios.usuarios import bp_usuarios
from .modules.colabs.colabs import bp_colabs

def create_app():
    app = Flask(__name__)
    secret = secrets.token_hex(32)
    app.config['SECRET_KEY'] = secret
    app.register_blueprint(bp_ti)
    app.register_blueprint(bp_usuarios)
    app.register_blueprint(bp_colabs)
    return app