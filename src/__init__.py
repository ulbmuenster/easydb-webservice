from . import TokenVerifier, TokenGenerator, API
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
import logging

# Logging config
logger = logging.getLogger("invser")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("invser.log")  # file logging
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()  # console logging
ch.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

# App configuration
app = Flask(__name__)
# Sets the secret needed for generating a JSONWebtoken.
app.config["SECRET_KEY"] = "\x18\x95\xf6\x86;\xb49m\xaa\xa5]\x9f\xf36\xa9\xc5"
api = Api(app)

# JWT configuration
jwt = JWTManager(app)
# Changes default behaviour and json responses of JWT-Extended.
# Source: https://flask-jwt-extended.readthedocs.io/en/latest/changing_default_behavior.html
@jwt.invalid_token_loader
@jwt.expired_token_loader
@jwt.needs_fresh_token_loader
def token_invalid(token):
    token_type = token['type']
    return jsonify({
        'status': 401,
        'msg': 'The {} token is invalid, expired or not fresh.'.format(token_type)
    }), 401


# Route configuration
# Tells flask_restful which script/class belongs to which request/URL
api.add_resource(TokenVerifier.TokenVerifier, "/TokenVerifier")
api.add_resource(TokenGenerator.TokenGenerator, "/TokenGenerator")
api.add_resource(API.API,"/generate")