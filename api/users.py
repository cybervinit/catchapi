from flask_restplus import Namespace, Resource, fields



api = Namespace('animals', description="animal operations")


@api.route('/')
class animalList(Resource):

	def get(self):
		return {
		'animal_name': 'Tiger',
		'age': 19
		}
		