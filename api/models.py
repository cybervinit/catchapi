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


user_stock_relationship_table = db.Table('user_stock_relationship_table', 
											db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False), 
											db.Column('stock_id', db.Integer, db.ForeignKey('stocks.id'), nullable=False),
											db.PrimaryKeyConstraint('user_id', 'stock_id'))


# Model class for Users
class User(BaseModel):
	__tablename__="users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False, unique=True)
	email = db.Column(db.String(120))
	country = db.Column(db.String(50))
	current_balance = db.Column(db.Integer, nullable=False)
	user_type = db.Column(db.Integer, nullable=False)
	current_net_worth = db.Column(db.Integer, nullable=False)
	stocks = db.relationship('Stock', secondary=user_stock_relationship_table, backref=db.backref('owners', lazy='dynamic'))
	new_worth_leaderboard = db.relationship('NetWorthLeaderboard', uselist=False, backref="user")


	def __init__(self, username, email, country, current_balance, user_type, current_net_worth):
		self.username = username
		self.email = email
		self.current_balance = current_balance
		self.user_type = user_type
		self.current_net_worth = current_net_worth
		self.country = country



class NetWorthLeaderboard(BaseModel):
	__tablename__="net_worth_leaderboard"

	id = db.Column(db.Integer, primary_key=True)
	rank = db.Column(db.Integer, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	username = db.Column(db.String(20), nullable=True)

	def __init__(self, rank, user_id, username):
		self.rank = rank
		self.user_id = user_id
		self.username = username


# Model class for Companies
class Company(BaseModel):
	__tablename__ = "companies"


	id = db.Column(db.Integer, primary_key=True)
	company_name = db.Column(db.String(32), nullable=False)
	current_owner = db.Column(db.String(20), nullable=True)
	stock_amount = db.Column(db.Integer)
	stock_price = db.Column(db.Integer)
	market_cap = db.Column(db.Integer)

	def __init__(self, company_name, current_owner, stock_amount, stock_price, market_cap):
		self.company_name = company_name
		self.current_owner = current_owner
		self.stock_amount = stock_amount
		self.stock_price = stock_price
		self.market_cap = market_cap


# Model class for Stocks
class Stock(BaseModel):
	__tablename__ = "stocks"

	id = db.Column(db.Integer, primary_key=True)
	company_name = db.Column(db.String(32), nullable=False)
	owner_user = db.Column(db.String(20), nullable=True)
	#owner = db.Column(db.String(20), nullable=True) # Nullable is true because initially, in the IPO, it is not owned. 

	def __init__(self, company_name, owner_user):
		self.company_name = company_name
		self.owner_user = owner_user







