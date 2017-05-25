from flask import Flask, render_template, request
from flask.ext.sqlalchemy import sqlalchemy

app = Flask(__name__)



@app.route('/')
def hello_world():
	return "This app has now started!"

