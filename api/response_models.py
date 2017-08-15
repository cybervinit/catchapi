from flask_restplus import Resource, fields
from testing import testEp


user_model = testEp.model('user', {
	'username': fields.String,
	'email': fields.String,
	'country': fields.String,
	'current_balance': fields.Integer,
	'user_type': fields.Integer,
	'current_net_worth': fields.Integer,
})


# user_list_model = {
# 	'users': fields.List
# }

