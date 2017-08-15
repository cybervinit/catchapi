from flask_restplus import Namespace, Resource, fields, reqparse
from models import db, User, Company, Stock, NetWorthLeaderboard
import models
from validator import validate, user_rank, username_validator, users_validator, net_worth_rank_validator, current_balance_rank_validator
from util import rank_types

usersApi = Namespace('users', description="User operations")


# ----------------------------------- Response Model Registration ------------------------------------------------------

user_model = usersApi.model('user', {
	'server_error': fields.String(default = "no"),
	'id': fields.Integer,
	'username': fields.String,
	'email': fields.String,
	'country': fields.String,
	'current_balance': fields.Integer,
	'user_type': fields.Integer,
	'current_net_worth': fields.Integer
})


# --------------------------------------------------- all users ---------------------------------------------

users_parser = reqparse.RequestParser()
users_parser.add_argument('amount', type=int)
users_parser.add_argument('rank_area', type=str) # 'top', 'bottom', or 'around' given user
users_parser.add_argument('username', type=str)

@usersApi.route('/')
@usersApi.response(522, 'Server broke :(')
@usersApi.response(222, 'success')
class users(Resource):

	def get(self):
		try:
			return {'server_error': 'TODO: setup respone which returns users around, top, bottom, etc'}, 322
			args = users_parser.parse_args()
			# ^^^^^^^^^^^ ERROR CHECK ^^^^^^^^^^^^^^^^^^^^^^^
			if (not validate(args, users_validator)):
				return {'server_error': 'one or more parameters not valid'}, 422
			if (not validate(args['username'], username_validator)):
				error_str = username+' does not exist.'
				return {'server_error': error_str}, 422
			# vvvvvvvvvvv ERROR CHECK END vvvvvvvvvvvvvvvvv
			
			return {'user': 'get users ordered by rank'}, 222
		except Exception as e:
			return {'server_error': str(e)}, 522

# --------------------------------------------------- General Rank ---------------------------------------------

@usersApi.route('/rank/')
class rank(Resource):

	def post(self):
		try:
			return {'message': 'here is where you add the user after making him'}, 322
		except Exception as e:
			return {'server_error': str(e)}, 522

	def put(self):
		try:
			update_rank_query = "UPDATE net_worth_leaderboard SET rank = new_t.rank FROM net_worth_leaderboard AS nwlb INNER JOIN (SELECT username, id, RANK() OVER(ORDER BY current_net_worth DESC) AS rank FROM users) AS new_t ON nwlb.user_id = new_t.id WHERE net_worth_leaderboard.user_id = new_t.id" 
			result = db.engine.execute(update_rank_query)
			return {'result': 'success!'}, 222
		except Exception as e:
			return {'server_error': str(e)}, 522

# --------------------------------------------------- given rank gets user ---------------------------------------------

rank_parser1 = reqparse.RequestParser()
rank_parser1.add_argument('rank_type')

@usersApi.route('/rank/<int:number>')
@usersApi.param('rank_type', 'specify a rank type')
class user_from_rank(Resource):

	@usersApi.marshal_with(user_model)
	def get(self, number):
		try:
			args = rank_parser1.parse_args()
			rank_type = args['rank_type']
			if rank_type == 'net_worth':
				# ^^^^^^^^^^^ ERROR CHECK ^^^^^^^^^^^^^^^^^^^^^
				if (not validate(number, net_worth_rank_validator)):
					return {'server_error': 'invalid rank number given'}, 422
				# vvvvvvvvvvv ERROR CHECK END vvvvvvvvvvvvvvvvv
				rank_user = NetWorthLeaderboard.query.filter_by(rank=number).first()
				user_username = rank_user.username
				user1 = User.query.filter_by(username=user_username).first()
				return user1, 222

			elif rank_type == 'current_balance':
				# ^^^^^^^^^^^ ERROR CHECK ^^^^^^^^^^^^^^^^^^^^^
				if (not validate(number, current_balance_rank_validator)):
					{'server_error': 'invalid rank number given'}, 422
				# vvvvvvvvvvv ERROR CHECK END vvvvvvvvvvvvvvvvv
				return {'server_error': 'TODO: return current balance rank of given user'}, 322

			return {'server_error': 'invalid rank type'}, 422
		except Exception as e:
			{'server_error': str(e)}, 522

# --------------------------------------------------- given username gets rank ---------------------------------------------
# get rank of a given user

rank_parser2 = reqparse.RequestParser()
rank_parser2.add_argument('rank_type')


# ROUTE
@usersApi.route('/<string:username>/rank/') 
# PARAMETERS
@usersApi.param('username', 'specify a user')
@usersApi.param('rank_type', 'specify a rank_type')
class rank_from_user(Resource):

	def get(self, username):
		try:
			args = rank_parser2.parse_args()

			# ^^^^^^^^^^^ ERROR CHECK ^^^^^^^^^^^^^^^^^^^^^^^
			if (not validate(args, user_rank)):
				return {'ERROR': 'one or more parameters not valid'}, 422
			if (not validate(username, username_validator)):
				error_str = username+' does not exist.'
				return {'ERROR': error_str}, 422
			# vvvvvvvvvvv ERROR CHECK END vvvvvvvvvvvvvvvvv

			rank_type = args['rank_type']

			if rank_type == 'net_worth':
				rankUser = NetWorthLeaderboard.query.filter_by(username=username).first()
				rank = rankUser.rank
				return {'rank': rank}, 222
			elif rank_type == 'current_balance':
				# TODO: return global rank of the user
				return {'TODO': 'get rank by current balance'}, 222
		except Exception as e:
			return {'SERVER ERROR': str(e)}, 522



# --------------------------------------------------- Registration ---------------------------------------------

registeringParser = reqparse.RequestParser()
registeringParser.add_argument('username', type=str)
registeringParser.add_argument('email', type=str)
registeringParser.add_argument('country', type=str)
registeringParser.add_argument('user_type', type=int)

register_fields = usersApi.model('Registration', {
	'username': fields.String,
	'email': fields.String,
	'country': fields.String, 
	'user_type': fields.Integer
	})

@usersApi.route('/register/')
@usersApi.response(522, 'Server broke :(')
@usersApi.response(222, 'success!')
class register(Resource):
	
	def get(self):
		try:
			return 'this is the registering page', 222
		except Exception as e:
			return {'message': str(e)}, 522


	@usersApi.expect(register_fields)
	def post(self):
		try:
			args = registeringParser.parse_args()
			db.session.add(User(username=args['username'], 
				email=args['email'],
				country=args['country'], 
				current_balance=100, 
				user_type=args['user_type'], 
				current_net_worth=100))
			db.session.commit()
			user1 = User.query.filter_by(username=args['username']).first()
			db.session.add(NetWorthLeaderboard(-1, user1.id, args['username']))
			db.session.commit()
			return {'message': 'success'}, 222
		except Exception as e:
			{'message': str(e)}, 522




# --------------------------------------------------- Exceptions ---------------------------------------------








