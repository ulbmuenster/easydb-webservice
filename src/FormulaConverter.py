from flask_restful import Resource
from flask import Response, request
import json


class FormulaGenerator(Resource):

	def post(self):
		try:
			post_data = request.get_json()
			if 'formula' in post_data:
				formula = post_data["formula"]
				# replace variations for Multiplication sign
				formula = formula.replace('*', '·')

				# set map for superstring and substring
				SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
				SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

				# set variables
				multiplicator = False
				convertedFormula = ''

				for i in range(len(formula)):
					if formula[i] == '·':
						multiplicator = True
					if formula[i].isalpha():
						multiplicator = False
					if formula[i].isdigit and not multiplicator:
						# handle free ions / charge
						if formula[i] == '+':
							convertedFormula = formula[:-1]
							convertedFormula = convertedFormula + formula[i-1].translate(SUP)
							convertedFormula = convertedFormula + "⁺"
						# handle number of atoms
						else:
							convertedFormula = convertedFormula + formula[i].translate(SUB)
					else:
						convertedFormula = convertedFormula + formula[i]

				return Response(json.dumps({"convertedFormula": convertedFormula}), status=200, mimetype='application/json')
			else:
				raise Exception("No formula given.")
		except Exception as err:
			return Response(json.dumps({"error": str(err)}), status=500, mimetype='application/json')