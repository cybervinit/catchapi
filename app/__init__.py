import os
from flask import Flask, render_template, request
from models import db


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)

import models # Must always be imported after the database because it requires the db to be initiated

form = """ 
<form action="/user" method="post">
	<input type="text" name="username"><br>
	<input type="text" name="email"><br>
	<input type="submit">
</form>"""

@app.route('/')
def hello_world():
	return "June 7, Wednesday. It's working"


@app.route('/user', methods=['POST', 'GET'])
def userpage():
	if (request.method == 'POST'):
		insert(request.form['username'], request.form['email'])
		return "The debugging is working!"
	else:
		return form #  render_template()

def insert(username, email):
	bobby = models.User(username, email)
	db.session.add(bobby)
	db.session.commit()





