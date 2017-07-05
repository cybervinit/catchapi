import os
from flask import Flask, render_template, request
from models import db
from flask_restplus import Resource, Api, fields, reqparse, Namespace

# namespace imports
from users import usersApi

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ App Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app = Flask(__name__)
api = Api(app)
api.title = 'CATCH API'
api.version = '1.0'
api.description = 'The api for an upcoming android application'
baseUrl = '/v1/'
app.config.from_object('config_app.DevelopmentConfig')
db.init_app(app)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Route setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
api.add_namespace(usersApi, path=baseUrl+'users')

import models # Must always be imported after the database because it requires the db to be initiated

# ~~~~~~~~~~~~ Person object ~~~~~~~~~~~~~~~~ 
class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age





# ------------------------------------------------------------------------------------------------ baseurl route ------------------------------------------------------------------------------------------------
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

	

	@api.marshal_with(model)
	def get(self, **kwargs):
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

