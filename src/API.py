from flask_restful import Resource
from flask_jwt_extended import fresh_jwt_required
from .IDGenerator import IDGenerator


class API(Resource):

    @fresh_jwt_required
    def post(self):
        # TODO Make the generation of the ID type dependent tttt
        id_gen = IDGenerator()
        return id_gen.generate()
