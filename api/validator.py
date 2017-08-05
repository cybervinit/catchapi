from util import rank_types
from models import db

# TODO

# ------------------------------ param validation ------------------------------

# general function to check all args, x, with a given function check()
def validate(x, check):
	return check(x)


def user_rank(args):
	# TODO: import values from util.py and check with those values!!
	if ((args['rank_type'] == None or args['rank_type'] == 'national' or args['rank_type'] == 'global')
		and (True)):
		return True
	else:
		return False


def username_validator(username):
	# check if the user exists in the database
	return False