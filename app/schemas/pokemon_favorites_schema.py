#ID pokemon
#ID usuario
from marshmallow import Schema, fields, ValidationError

class FavoriteSchema(Schema):
    usuario_id = fields.Str(
        required=True,
        validate=lambda x: len (x) > 0,
        error_messages={
            "required":"El Id de pokemon es requerido"
        }
    )

    pokemon_id = fields.Str(
        required=True,
        validate=lambda x: len (x) > 0,
        error_messages={
            "required":"El Id de usuario es requerido"
        }
    )