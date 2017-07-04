import os



class BaseConfig(object):
	TESTING = False
	SQLALCHEMY_DATABASE_URI = ''



class DevelopmentConfig(BaseConfig):
	FLASK_DEBUG=True
	basedir = os.path.abspath(os.path.dirname(__file__))
	SQLALCHEMY_DATABASE_URI = 'postgresql:///' +'newdb' #os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
	DEBUG=False
	dbInfo = {}
	dbInfo["user"] = 'cdtaklgsbeqdbc'
	dbInfo["password"] = '4b07ec79528edb632391d36ac98a30df1372a566b241e69e5c128f52490b75c4'
	dbInfo["dbname"] = 'd1su5tfgru1p6m'
	dbInfo["port"] = '5432'
	dbInfo["host"] = 'ec2-50-17-236-15.compute-1.amazonaws.com'
	SQLALCHEMY_DATABASE_URI = 'postgresql://'+dbInfo['user']+':'+dbInfo['password']+'@'+dbInfo['host']+':'+dbInfo['port']+'/'+dbInfo['dbname']

