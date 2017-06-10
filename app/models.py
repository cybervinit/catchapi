from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class BaseModel(db.Model):

	__abstract__ = True

	
	def __repr__(self):
		return '%s(%s)' % (self.__class__.__name__, {
    		column: value
    		for column, value in self._to_dict().items()
    	})
	""" 
    	Can also add a method to JSONify objects
	"""


class User(BaseModel):
	__tablename__="users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), nullable=True)


	def __init__(self, name, email):
		self.name = name
		self.email = email

