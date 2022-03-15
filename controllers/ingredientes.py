from flask_restful import Resource, request

class IngesdioentesController(Resource):
    def get(self):
        return {
            'message' : 'yo soy el get de los ingredientes'
        }
    def post(self):
        print(request.get_json())
        return {
            'message': 'Yo soy el post'
        }
        