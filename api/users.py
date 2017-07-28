from flask_restplus import Namespace, Resource, fields
from models import db
import models


usersApi = Namespace('users', description="User operations")


@usersApi.route('/')
@usersApi.response(500, 'Server broke :(')
@usersApi.response(200, 'success')
class users(Resource):

	def get(self):
		try:
			# get users
			return {'user': 'vinit'}, 200
		except Exception as e:
			return {'message': str(e)}, 500
	
	
	def post(self):
		return 'work', 200
