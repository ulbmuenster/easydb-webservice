from flask_restful import Resource
from flask_jwt_extended import create_access_token


class TokenGenerator(Resource):

	def get(self):
		# Simply generates a JSONWebToken with the secret set in config.py with the extra information that the
		# generated token is a fresh token. expires_delta=False sets the expiration time to infinite.
		return create_access_token("easydb5", expires_delta=False)
