from util import rank_types
from models import db, User

# TODO

# ------------------------------ param validation ------------------------------

# general function to check all args, x, with a given function check()
def validate(x, check):
	return check(x)


def user_rank(args):
	# TODO: import values from util.py and check with those values!!
	if ((args['rank_type'] in rank_types)
		and (True)): # more conditions
		return True
	else:
		return False


def username_validator(username):
	# check if the user exists in the database
	user = User.query.filter_by(username=username).first()
	if (user is None):
		return False
	return True

def users_validator(args):
	if (args['amount'] >= 0):
		if (args['rank_area'] == 'top' or args['rank_area'] == 'bottom'):
			return True
		elif (args['rank_area'] == 'around_user'):
			if (not args['username'] == None):
				return True

	return False
