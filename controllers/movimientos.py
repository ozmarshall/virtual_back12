from flask_restful import Resource, request
from models.movimientos import Movimiento
from dtos.movimiento_dto import MovimientoRequestDTO, MovimientoResponsetDTO
from flask_jwt import jwt_required, current_identity
from config import conexion


class MovimientoController(Resource):


    @jwt_required()
    def post(self):
        body = request.get_json()
        try:
            print(current_identity)
            
            data = MovimientoRequestDTO().load(body)
            data['usuario_id'] = current_identity.id
            nuevoMovimiento = Movimiento(**data)
            conexion.session.add(nuevoMovimiento)
            conexion.session.commit()
            resultado = MovimientoResponsetDTO().dump(nuevoMovimiento)
            return {
                'message': 'Movimiento creado existosamente',
                'content' : resultado
            }, 201

        except Exception as e:

            return {
                'message': 'Error al crear el movimiernto',
                'content': e.args
            }

    @jwt_required()
    def get(self):
        current_identity

        movimientos : list[Movimiento] = conexion.session.query(Movimiento).filter_by(usuario_id = current_identity.id).all()

        resultado = MovimientoResponsetDTO(many=True).dump(movimientos)

        return {
            'message' : 'Los movimientos son',
            'content' : resultado
        }

        pass
