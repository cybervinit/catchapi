import os
from flask import Flask, render_template, request, jsonify
from flask.json import JSONEncoder
from models import db, User, Stock, Company, NetWorthLeaderboard
from flask_restplus import Resource, Api, fields, reqparse, Namespace

# namespace imports
from .users import usersApi as usersEp
from .companies import companiesApi as companiesEp
from .stocks import stocksApi as stocksEp
from .testing import testEp # testing

# seeding
from seeder import user_seed_list, nwLb_seed_list, stock_seed_list

# validations
from validator import validate, seed_validator


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ App Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app = Flask(__name__)
api = Api(app)
api.title = 'CATCH API'
api.version = '1.0'
api.description = 'The api for an upcoming android application'
baseUrl = '/v1/'
app.config.from_object('config_app.ProductionConfig')
db.init_app(app)
import models # Must always be imported after the database because it requires the db to be initiated
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Route setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
api.add_namespace(usersEp, path=baseUrl+'users') 		  # USERS
api.add_namespace(companiesEp, path=baseUrl+'companies')  # COMPANIES
api.add_namespace(stocksEp, path=baseUrl+'stocks')		  # STOCKS
api.add_namespace(testEp, path=baseUrl+'test')            # testing

# ------------------------------------ baseurl route --------------------
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('age', type=int)

@api.route(baseUrl)
@api.expect(parser)
class main_page(Resource):

	model = api.model('Model', {
		'name': fields.String(default="No name"),
		'age': fields.Integer(default=18)
		})

	def get(self, **kwargs):
		return 'The first version of the api.'
		args = parser.parse_args(strict=True)
		try:
			# Here is where you get the api info
			if kwargs is not None:
				return Person(name=args.get('name', 'noname'), age=args.get('age', -1))
			else:
				return "none"
		except:
			# error caught
			return 'error'


# ----------------------------------- seeding --------------------------




seedParser = reqparse.RequestParser()
seedParser.add_argument('seed_type', location='args') # one of users, stocks, companies, net_worth_leaderboard...

@api.route(baseUrl+'seed/')
#PARAMS
@api.param('seed_type', 'specify which table to seed')
class seeding(Resource):
	def get(self):
		return {'message': 'seeding area'}

	def post(self):
		try:
			args = seedParser.parse_args()
			if (not validate(args, seed_validator)):
				return {'ERROR': 'arguments may not be valid'}, 422
			# Add the appropriate data
			seedAt(args['seed_type'])
			return {'message': 'success'}, 222
		except Exception as e:
			return {'message': str(e)}, 522

	def delete(self):
		try:
			args = seedParser.parse_args()
			if (not validate(args, seed_validator)):
				return {'ERROR': 'arguments may not be valid'}, 422
			removeAt(args['seed_type'])
			return {'message': 'deleted'}, 222
		except Exception as e:
			return {'SERVER ERROR': str(e)}, 522


def seedAt(dbName):
	if dbName=='users':
		for user in user_seed_list:
			db.session.add(user)
	elif dbName=='stocks':
		for stock in stock_seed_list:
			db.session.add(stock)
		pass
	elif dbName=='companies':
		# companies stuff
		pass
	elif dbName=='user_stock_relationship_table':
		pass
	elif dbName=='net_worth_leaderboard':
		for user in nwLb_seed_list:
			db.session.add(user) 
	db.session.commit()

def removeAt(dbName):
	if (dbName=='users'):
		for user in user_seed_list:
			User.query.filter_by(username=user.username).delete()
	elif (dbName=='stocks'):
		for stock in stock_seed_list:
			Stock.query.filter_by(company_name=stock.company_name).delete()
	elif (dbName=='companies'):
		# companies stuff
		pass
	elif (dbName == 'net_worth_leaderboard'):
		for user in nwLb_seed_list:
			NetWorthLeaderboard.query.filter_by(user_id=user.user_id).delete()
	db.session.commit()


























