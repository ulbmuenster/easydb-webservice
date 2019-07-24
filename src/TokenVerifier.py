from flask import Response
from flask_restful import Resource
from flask_jwt_extended import fresh_jwt_required
import json


class TokenVerifier(Resource):

    # @fresh_jwt_required is needed to tell jwt-extended that the JSONWebToken has to be fresh and valid in order
    # for the function to be executed.
    @fresh_jwt_required
    def post(self):
        message = json.dumps({'status': 200, 'msg': "The access token is valid."})
        return Response(message, status=200, mimetype='application/json')
