from flask_restplus import Namespace, Resource, fields, reqparse
from models import db, User, Company, Stock
import models


usersApi = Namespace('users', description="User operations")

# --------------------------------------------------- all users ---------------------------------------------

@usersApi.route('/')
@usersApi.response(522, 'Server broke :(')
@usersApi.response(222, 'success')
class users(Resource):

	def get(self):
		try:
			# get users
			return {'user': 'vinit'}, 222
		except Exception as e:
			return {'message': str(e)}, 522
	
	
	def post(self):
		return 'work', 222

# --------------------------------------------------- rank ---------------------------------------------


rank_parser = reqparse.RequestParser()
rank_parser.add_argument('rank_type')

# ROUTE
@usersApi.route('/<string:username>/rank/') 
# RESPONSE TYPES
@usersApi.response(522, 'server broke :(')
@usersApi.response(222, 'success')
@usersApi.response(422, 'not found')
# PARAMETERS
@usersApi.param('username', 'specify a user')
@usersApi.param('rank_type', 'specify a rank_type')
class rank(Resource):

	def get(self, username):
		try:
			# assert that all args exist in DB or are valid
			args = rank_parser.parse_args()
			if (args['rank_type'] == None or args['rank_type'] == 'national'):
				return {'rank_type': 'national rank'}, 222
			elif args['rank_type'] == 'global':
				return {'rank_type': 'global rank'}, 222
			return {'ERROR': 'must specify valid rank_type'}, 422
		except Exception as e:
			return {'SERVER ERROR': str(e)}, 522

	def post(self):
		pass



# --------------------------------------------------- Registration ---------------------------------------------

registeringParser = reqparse.RequestParser()
registeringParser.add_argument('username', type=str, location='form')
registeringParser.add_argument('email', type=str, location='form')
registeringParser.add_argument('country', type=str, location='form')

@usersApi.route('/register/')
@usersApi.response(522, 'Server broke :(')
@usersApi.response(222, 'success!')
class register(Resource):
	
	def get(self):
		try:
			return 'this is the registering page', 222
		except Exception as e:
			return {'message': str(e)}, 522


	def post(self):
		try:
			args = registeringParser.parse_args()
			db.session.add(User(username=args['username'], email=args['email'], country=args['country'], current_balance=100, user_type=1, current_net_worth=100))
			db.session.commit()
			return {'message': 'success'}, 222
			# return {'message': 'user made'}, 200
		except Exception as e:
			{'message': str(e)}, 522




# --------------------------------------------------- Exceptions ---------------------------------------------








