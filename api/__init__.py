import os
from flask import Flask, render_template, request
from models import db
from flask_restplus import Resource, Api, fields, reqparse

from .users import api as ns1

app = Flask(__name__)
api = Api(app)
# app.config.from_pyfile('config.py')
# FIX THE CONFIGURATION ERROR! 
baseUrl = '/v1'
app.config.from_object('config_app.DevelopmentConfig')
db.init_app(app)
api.add_namespace(ns1, baseUrl+'/animals')

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
		'age': fields.Integer
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


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------ v1/users section ------------------------------------------------------------------------------------------------
@api.route(baseUrl+'/users')
class users(Resource):
	def get(self):
		try:
			# get users
			pass
		except:
			# in case of exception
			pass
		return {'get': 'works'}


	def post(self):
		try:
			# put in the new user
			pass
		except:
			return {'error': 'some error'}
			pass

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

