from flask_restful import Resource, request
from models.preparaciones import Preparacion
from dtos.preparacion_dto import PreparacionesRequestDTO, PreparacionesResponseDTO
from config import conexion

class PreparacionesController(Resource):
    def post(self):
        try:
            body = request.get_json()
            data = PreparacionesRequestDTO().load(body)
            print(data)
            nuevaPreparacion = Preparacion(**data)
            conexion.session.add(nuevaPreparacion)
            conexion.session.commit()
            respuesta = PreparacionesResponseDTO().dump(nuevaPreparacion)

            return {
                'message': 'Preparacion creada exitosamente',
                'preparacion' : respuesta
            }, 201

        except Exception as e:
            conexion.session.rollback()
            return {
                'message':'hubo un error al crear la preparcion',
                'content': e.args
            }, 404

    def get(self):
        
        preparacion : Preparacion| None = conexion.session.query(Preparacion).filter_by(id=1).first()
        print(preparacion)
        print(preparacion.orden)
        print(preparacion.receta.nombre)
        print(preparacion.receta_id)

        return {
            'message': 'ok'
        }