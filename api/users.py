from flask_restplus import Namespace, Resource, fields, reqparse
from models import db, User, Company, Stock
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



registeringParser = reqparse.RequestParser()
registeringParser.add_argument('username', type=str, location='form')
registeringParser.add_argument('email', type=str, location='form')
registeringParser.add_argument('country', type=str, location='form')

@usersApi.route('/register/')
@usersApi.response(500, 'Server broke :(')
@usersApi.response(200, 'success!')
class register(Resource):
	def get(self):
		try:
			return 'this is the registering page', 200
		except Exception as e:
			return {'message': str(e)}, 500


	def post(self):
		try:
			args = registeringParser.parse_args()
			db.session.add(User(username=args['username'], email=args['email'], country=args['country'], current_balance=100, user_type=1, current_net_worth=100))
			db.session.commit()
			return {'message': 'success'}, 200
			# return {'message': 'user made'}, 200
		except Exception as e:
			{'message': str(e)}, 500
