from flask_restplus import Namespace, Resource, fields
from models import db
import models

companiesApi = Namespace('companies', description='Company operations')

@companiesApi.route('/')
@companiesApi.response(500, 'Server broke :(')
@companiesApi.response(200, 'success')
class companies(Resource):

	def get(self):
		try:
			# get companies
			return {'companies': 'Google, Facebook...'}, 200
		except Exception as e:
			return {'message': str(e)}, 500

	def post(self):
		pass