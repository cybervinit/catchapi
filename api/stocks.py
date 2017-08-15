from flask_restplus import Namespace, Resource, fields, reqparse
from models import db, User, Stock
import models
from validator import validate, username_validator

stocksApi = Namespace('stocks', description="Stock operations")

# ----------------------------------- Response Model Registration ------------------------------------------------------

stock_model = stocksApi.model('stock', {
	'server_error': fields.String(default = "no"),
	'company_name': fields.String
	})

stock_list_model = stocksApi.model('stocks', {
	'server_error': fields.String(default = "no"),
	'stocks': fields.List(fields.Nested(stock_model))
	})

# -----------


@stocksApi.route('/')
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


# --------------------------------------------------- Given username Get owned Stocks ---------------------------------------------



@stocksApi.route('/<string:username>')
class user_stocks(Resource):

	@stocksApi.marshal_with(stock_list_model)
	def get(self, username): 
		try:
			# ^^^^^^^^^^^ ERROR CHECK ^^^^^^^^^^^^^^^^^^^^^
			if (not validate(username, username_validator)):
				return {'server_error': 'invalid username given'}, 422
			# vvvvvvvvvvv ERROR CHECK END vvvvvvvvvvvvvvvvv
			user1 = User.query.filter_by(username=username).first()
			user1_id = user1.id
			get_stock_list_query = "SELECT company_name FROM stocks WHERE owner_user = '%s' GROUP BY company_name" % (username)
			stock_list_result = db.engine.execute(get_stock_list_query)
			stock_list = []
			for stock in stock_list_result:
				stock_list.append(stock)
			
			return {'stocks': stock_list}, 222

		except Exception as e:
			return {'server_error': str(e)}, 522
