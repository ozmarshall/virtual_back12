
from config import validador
from models.preparaciones import Preparacion
from models.recetas import Receta
from marshmallow import fields
from dtos.receta_dto import RecetaResponseDTO

class PreparacionesRequestDTO (validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Preparacion
        include_fk = True

class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta       

class PreparacionesResponseDTO (validador.SQLAlchemyAutoSchema):
    receta = fields.Nested(nested=RecetaResponseDTO, data_key = 'receta_relacion')
    class Meta:
        model = Preparacion
        load_instance = True
        include_fk = False
        include_relationships = True