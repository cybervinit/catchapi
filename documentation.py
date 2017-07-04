import os
from flask import Flask, render_template, request
from models import db
from flask_restplus import Resource, Api, fields, reqparse


# app = Flask(__name__)
# api = Api(app)
# app.config.from_object('config.DevelopmentConfig')
# db.init_app(app)
baseUrl = '/v1'



# REQUEST PARSING FOR READING URL PARAMETERS  --> ('<url>?name=vinit&age=19...')  --------------------------------------------------

blogReqParser = reqparse.RequestParser()
blogReqParser.add_argument('blog_id', type=int, help="bad choice of value or null", required=bool, action='append', dest='blogId')

# add_argument --> adds the parameter as a part of the URL
# '<name>'     --> name of the parameter
# type         --> parameter type
# help         --> returns this string in case of error
# required     --> if parameter is required or not
# action       --> if the client wants to send a list
# dest         --> what the new name of the parameter should be, once called

# -----------------------------------------------------------------------------------------------------------------------------------


@api.route('/hello')                  # creates the api route to this function
@api.expect(blogReqParser)            # sets the parameters which can be fetched with this url
class helloUser(Resource):

	blog_model = api.model('blog model', {                  # models defined as a JSON skeleton, which should be used to return responses
		'blog_name': fields.String(default="No name")       # default, if the blog_name not given
		'blog_id': fields.Integer
		})

	@api.marshal_with(blog_model)
	def get(self, **kwargs):          # defines the get endpoint for this url
		args = blogReqParser.parse_args(strict=True)        # parses all the parameters, and throws the error if extra, undefined arguments are present
		blogId = args.get('blogId', -1)
		return {											# marshalling works with single objects, dicts, or list of objects!
				'blog_name': 'Vinit\' Blog',
				'blog_id': blogId
			}





