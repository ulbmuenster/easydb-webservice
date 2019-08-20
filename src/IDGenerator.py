from flask_jwt_extended import jwt_required
from .Models import Inventarnummer, Institution, db
from flask_restful import Resource
from flask import Response, request, current_app
import json


class IDGenerator(Resource):

	@jwt_required
	def post(self):
		try:
			post_data = request.get_json()
			if post_data:
				post_prefix = post_data["prefix"]
				post_institution = post_data["institution"]

				# Check if the abbreviation or the full name of the institution has been sent and if one of them
				# returns a row from the institution table.
				db_institution = Institution.query.filter_by(institution_abbrev=post_institution).first()
				if not db_institution:
					db_institution = Institution.query.filter_by(institution_full=post_institution).first()

				# No institution could be found, return an Exception.
				if not db_institution:
					raise Exception("Institution does not exist.")

				# Assignment of value to variables for easier usage
				inst_id = db_institution.id
				institution_abbrev = db_institution.institution_abbrev
				min_number = db_institution.min_number
				max_number = db_institution.max_number
				invnr_format = db_institution.format
				last_inv_id = Inventarnummer.query.order_by(Inventarnummer.id.desc()).\
					filter_by(prefix=post_prefix, institution_id=inst_id).limit(1).first()

				# Check if an id has already been generated and count up from that, otherwise start generating in the
				# specified number range starting with the minimum that is defined.
				if last_inv_id:
					if last_inv_id.id < max_number:
						generated_invnr = Inventarnummer(id=last_inv_id.id+1, institution_id=inst_id, prefix=post_prefix)
						pass
					else:
						raise Exception("Could generate id, number range is full.")
				else:
					generated_invnr = Inventarnummer(id=min_number, institution_id=inst_id, prefix=post_prefix)
					pass
				db.session.add(generated_invnr)
				db.session.commit()

				# "Build" the response/inventory number with the given/specified format
				response_id = invnr_format
				response_id = response_id.replace("INSTITUTION", institution_abbrev)
				response_id = response_id.replace("PREFIX", post_prefix)
				response_id = response_id.replace("ID", str(generated_invnr.id))
				return Response(json.dumps({"invnr": response_id}), status=200, mimetype='application/json')
			else:
				# If no post_data has been sent, raise an exception.
				raise Exception("No post data has been sent!")
		except Exception as err:
			return Response(json.dumps({"error": str(err)}), status=500, mimetype='application/json')
