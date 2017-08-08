from flask_restplus import Namespace, Resource, fields, reqparse
from models import db, User, Company, Stock
import models
from validator import validate, user_rank, username_validator, users_validator
from util import rank_types


usersApi = Namespace('users', description="User operations")

# --------------------------------------------------- all users ---------------------------------------------

users_parser = reqparse.RequestParser()
users_parser.add_argument('amount', type=int)
users_parser.add_argument('rank_area', type=str)
users_parser.add_argument('username', type=str)

@usersApi.route('/')
@usersApi.response(522, 'Server broke :(')
@usersApi.response(222, 'success')
class users(Resource):

	def get(self):
		try:
			args = users_parser.parse_args()
			# ^^^^^^^^^^^ ERROR CHECK ^^^^^^^^^^^^^^^^^^^^^^^
			if (not validate(args, users_validator)):
				return {'ERROR': 'one or more parameters not valid'}, 422
			if (not validate(args['username'], username_validator)):
				error_str = username+' does not exist.'
				return {'ERROR': error_str}, 422
			# vvvvvvvvvvv ERROR CHECK END vvvvvvvvvvvvvvvvv

			
			return {'user': 'get users ordered by rank'}, 222
		except Exception as e:
			return {'SERVER ERROR': str(e)}, 522
	
	
	def post(self):
		return {'action': 'update the ranks of the users'}, 222

# --------------------------------------------------- Rank ---------------------------------------------


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
			args = rank_parser.parse_args()

			# ^^^^^^^^^^^ ERROR CHECK ^^^^^^^^^^^^^^^^^^^^^^^
			if (not validate(args, user_rank)):
				return {'ERROR': 'one or more parameters not valid'}, 422
			if (not validate(username, username_validator)):
				error_str = username+' does not exist.'
				return {'ERROR': error_str}, 422
			# vvvvvvvvvvv ERROR CHECK END vvvvvvvvvvvvvvvvv
			
			rank_type = args['rank_type']

			if args['rank_type'] == 'national':
				#TODO: return national rank of the user
				return {'rank_type': 'national rank'}, 222
			elif args['rank_type'] == 'global':
				# TODO: return global rank of the user
				return {'rank_type': 'global rank'}, 222
		except Exception as e:
			return {'SERVER ERROR': str(e)}, 522


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








