from src import TokenVerifier, TokenGenerator, IDGenerator
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # Load the configuration from the config folder
    app.config.from_object("cfg.default")
    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')
    # Load the file specified by the APP_CONFIG_FILE environment variable
    # Variables defined here will override those in the default configuration
    # app.config.from_envvar('APP_CONFIG_FILE')
    app.config.from_object("cfg.development")
    # SQLAlchemy
    from src.InventarnummerModel import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # Flask-Restful API
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
            'error': 'The {} token is invalid, expired or not fresh.'.format(token_type)
        }), 401
    # Route configuration
    # Tells flask_restful which script/class belongs to which request/URL
    api.add_resource(TokenVerifier.TokenVerifier, "/TokenVerifier")
    api.add_resource(TokenGenerator.TokenGenerator, "/TokenGenerator")
    api.add_resource(IDGenerator.IDGenerator, "/generate")

    return app
