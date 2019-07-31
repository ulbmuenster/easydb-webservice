from flask_jwt_extended import jwt_required
from .InventarnummerModel import db, Inventarnummer
from flask_restful import Resource
from flask import Response, request, jsonify, current_app
import json


class IDGenerator(Resource):

    @jwt_required
    def post(self):
        try:
            post_data = request.get_json()
            if post_data:
                prefix = post_data["prefix"]
                institution = post_data["institution"]
                id = Inventarnummer.query.order_by(Inventarnummer.id.desc()).filter_by(prefix=prefix).limit(1).first()
                if id:
                    generated_id = Inventarnummer(id=id.id+1, institution=institution, prefix=prefix)
                else:
                    generated_id = Inventarnummer(id=1, institution=institution, prefix=prefix)
                db.session.add(generated_id)
                db.session.commit()
                response_id = current_app.config["GENERATED_ID_FORMAT"]
                response_id = response_id.replace("INSTITUTION", institution)
                response_id = response_id.replace("PREFIX", prefix)
                response_id = response_id.replace("ID", str(generated_id.id))
                return Response(json.dumps({"id": response_id}), status=200, mimetype='application/json')
        except Exception as err:
            return Response(json.dumps({"error": str(err)}), status=500, mimetype='application/json')
