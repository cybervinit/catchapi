from flask_restplus import Namespace, Resource, fields
from models import db
import models


stocksApi = Namespace('stocks', description="Stock operations")

@stocksApi.route('/')
@stocksApi.response(500, 'stocks endpoint broke')
@stocksApi.response(200, 'success')
class stocks(Resource):

	def get(self):
		try:
			#get stocks
			return db.session.query.filter_by(email='vinit@gmail.com'), 200
		except Exception as e:
			return {'message': str(e)}, 500


	def post(self):
		try:
			return {'message': 'success'}, 200
		except Exception as e:
			return {'message': str(e)}, 500