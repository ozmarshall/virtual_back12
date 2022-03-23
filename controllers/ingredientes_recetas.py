from flask_restful import Resource, request
from models.ingredientes_recetas import IngredientesRecetas
from dtos.ingredientes_recetas_dto import IngredientesRecetasRequestDTO
from config import conexion

class IngredientesRecetasController(Resource):
    def post(self):
        body = request.get_json()
        try: 
            data = IngredientesRecetasRequestDTO().load(body)
            nuevoIR = IngredientesRecetas(**data)
            conexion.session.add(nuevoIR)
            conexion.session.commit()

            return {
                'message': 'Ingrediente-receta agregado exitosamente'
            } ,201

        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'error al ingresar el ingrediente-reeceta',
                'content': e.args
            }, 400