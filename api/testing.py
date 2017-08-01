from flask_restplus import Namespace, Resource, fields, reqparse
from models import db, User, Company, Stock
import models
from flask import jsonify, make_response

testEp = Namespace('testing', description='testing env')


parser = reqparse.RequestParser()
parser.add_argument('age', type=int)

@testEp.route('/')
@testEp.response(500, 'Server broke :(')
@testEp.response(200, 'success')
class tests(Resource):

	def get(self):
		args = parser.parse_args()
		return {'age': args['age']}, 222

	def post(self):
		pass
		#testing