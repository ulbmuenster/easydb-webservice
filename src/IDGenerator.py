from flask_jwt_extended import jwt_required
from .InventarnummerModel import db, Inventarnummer
from flask_restful import Resource
from flask import Response, jsonify
import json


class IDGenerator(Resource):

    @jwt_required
    def get(self):
        try:
            id = Inventarnummer.query.order_by(Inventarnummer.id.desc()).limit(1).first()
            if id:
                generated_id = Inventarnummer(id=id.id+1)
            else:
                generated_id = Inventarnummer(id=1)
            db.session.add(generated_id)
            db.session.commit()
            return Response(json.dumps({"id": generated_id.id}), status=200, mimetype='application/json')
        except DatabaseError as err:
            return Response(json.dumps({"error": err.message()}), status=500, mimetype='application/json')
        except DisconnectionError as err:
            return Response(json.dumps({"error": err.message()}), status=503, mimetype='application/json')
