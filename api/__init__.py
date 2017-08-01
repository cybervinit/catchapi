import os
from flask import Flask, render_template, request, jsonify
from flask.json import JSONEncoder
from models import db, User, Stock, Company
from flask_restplus import Resource, Api, fields, reqparse, Namespace

# namespace imports
from .users import usersApi as usersEp
from .companies import companiesApi as companiesEp
from .stocks import stocksApi as stocksEp
from .testing import testEp # testing

# seeding
from seeder import userList

# ---------------------------------- Custom JSON serializer ----------------------------

class CatchJSONEncoder(JSONEncoder):
	def default(self, obj):
		if isinstance(obj, User):
			return {
				'username': obj.username,
				'email': obj.email,
				'country': obj.country,
				'current_balance': obj.current_balance,
				'user_type':obj.user_type,
				'current_net_worth': obj.current_net_worth
			}
		if isinstance(obj, Stock):
			return {
				'company_name': obj.company_name
			}
		# TODO: add the other object classifications
		return JSONEncoder.default(self, obj)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ App Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app = Flask(__name__)
app.json_encoder = CatchJSONEncoder
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






# --------------------------------------------------- baseurl route --------------------------------------
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


# --------------------------------------------------- seeding ---------------------------------------------




seedParser = reqparse.RequestParser()
seedParser.add_argument('seed_type') # one of users, stocks, companies...
seedParser.add_argument('action_type') # one of add, remove

@api.route(baseUrl+'seed/')
class seeding(Resource):
	def get(self):
		return {'message': 'seeding area'}

	def post(self):
		try:
			args = seedParser.parse_args(strict=True)
			if (args['seed_type'] == 'users' or 
				args['seed_type'] == 'stocks' or 
				args['seed_type'] == 'companies'):
				if (args['action_type'] == 'add'):
					# Add the appropriate data
					seedAt(args['seed_type'])
					return {'message': 'success'}, 222
				elif (args['action_type'] == 'remove'):
					# delete the data
					removeAt(args['seed_type'])
					return {'message': 'success'}, 222

			return {'message': 'wrong types given'}, 422				
		except Exception as e:
			return {'message': str(e)}, 500




def seedAt(dbName):
	if dbName=='users':
		for user in userList:
			db.session.add(user)
	elif dbName=='stocks':
		#stock stuff
		pass
	elif dbName=='companies':
		# companies stuff
		pass
	db.session.commit()

def removeAt(dbName):
	if (dbName=='users'):
		for user in userList:
			db.session.delete(user)
	elif (dbName=='stocks'):
		#stock stuff
		pass
	elif (dbName=='companies'):
		# companies stuff
		pass
	db.session.commit()


























