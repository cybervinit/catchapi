from flask_restplus import Namespace, Resource, fields, reqparse
from models import db, User, Company, Stock
import models
from flask import jsonify, make_response

testEp = Namespace('testing', description='testing env')

@testEp.route('/')
@testEp.response(500, 'Server broke :(')
@testEp.response(200, 'success')
class tests(Resource):

	def get(self):
		result1 = db.engine.execute("select * from users where username='sejal' or username='vinit'")
		name = []
		for row in result1:
			name.append(User(row[5], row[1], row[6], row[2], row[4], row[3]))
		return jsonify(name)
		#testing

	def post(self):
		pass
		#testing