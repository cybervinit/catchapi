from flask_restplus import Namespace, Resource, fields, reqparse, marshal
from models import db, User, Company, Stock
import models
from flask import jsonify, make_response
import os

testEp = Namespace('testing', description='testing env')

# --------------- Response Model Registration ----------------

# ----------------------------- base response model ----------------------
base_response_model1 = testEp.model('parent', {
	'server_error': fields.String(default="no")
	})

test_model = testEp.model('test', {
	'server_error': fields.String(default="no"),
	'id': fields.Integer,
	'username': fields.String,
	'email': fields.String,
	'country': fields.String,
	'current_balance': fields.Integer,
	'user_type': fields.Integer,
	'current_net_worth': fields.Integer,
})


user_list_model = testEp.model('userList', {
	'server_error': fields.String(default="no"),
	'users': fields.List(fields.Nested(test_model))
})

# ------------------------------------------------------------

parser = reqparse.RequestParser()
parser.add_argument('age', type=int)

age_fields = testEp.model('Age', {'age': fields.Integer})

@testEp.route('/')
class tests(Resource):

	@testEp.marshal_with(user_list_model)
	def get(self):
		try:
			args = parser.parse_args()
			user1 = User(username='vinitsoni', email='soni@gmail.com', country='canada', current_balance=122, user_type=22, current_net_worth=124)
			user2 = User(username='sonivinit', email='soni@gmail.com', country='canada', current_balance=122, user_type=22, current_net_worth=124)
			arr = []
			arr.append(user1)
			arr.append(user2)
			arr.append(User.query.filter_by(username='vinit').first())
			return {'users': arr}, 222
			return {'server_error': 'asdf'}, 422
		except Exception as e:
			return {'server_error': str(e)}, 522


	@testEp.expect(age_fields)
	def post(self):
		args = parser.parse_args()
		m = args['age'] + 1
		return {'age': m}, 222
