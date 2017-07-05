from flask_restplus import Namespace, Resource, fields
from models import db
import models


usersApi = Namespace('users', description="User operations")


@usersApi.route('/')
class users(Resource):

	def get(self):
		# get users
		return models.Stock.query.Jsonify()
	
	def post(self):
		pass
