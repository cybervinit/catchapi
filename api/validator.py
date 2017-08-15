from util import seed_types, rank_types
from models import db, User, NetWorthLeaderboard

# TODO

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< VALIDATION >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# general function to check all args, x, with a given function check()
def validate(x, check):
	return check(x)

# --------------------------------- USERS ---------------------------------


def username_validator(username):
	# check if the user exists in the database
	user = User.query.filter_by(username=username).first()
	if (user is None):
		return False
	return True

def user_rank(args):
	# TODO: import values from util.py and check with those values!!
	if ((args['rank_type'] in rank_types)
		and (True)): # more conditions
		return True
	else:
		return False


def users_validator(args):
	if (args['amount'] >= 0):
		if (args['rank_area'] == 'top' or args['rank_area'] == 'bottom'):
			return True
		elif (args['rank_area'] == 'around_user'):
			if (not args['username'] == None):
				return True
	return False

def net_worth_rank_validator(number):
	rank_user = NetWorthLeaderboard.query.filter_by(rank=number).first()
	if rank_user:
		return True
	return False

def current_balance_rank_validator(number):
	# TODO
	return True

# --------------------------------- STOCKS ---------------------------------



# --------------------------------- SEED ---------------------------------

def seed_validator(args):
	if (args['seed_type'] in seed_types):
		return True
	return False

