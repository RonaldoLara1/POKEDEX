from flask import Blueprint, request, jsonify
from app.models.factory import ModelFactory
from bson import ObjectId
from marshmallow import ValidationError
from app.schemas.user_schema import UserSchema 
from app.tools.response_manager import ResponseManager
from app.schemas.pokemon_favorites_schema import FavoriteSchema

RM = ResponseManager()
bp = Blueprint('user_controller', __name__, url_prefix='/favorite-pokemons')
FP_MODEL = ModelFactory.get_model("pokemon_favorites")
FP_SCHEMA = FavoriteSchema()


@bp.route('/', methods=['POST'])
def create():
    try:
        data = request.json
        data= FP_SCHEMA.validate(data)
        fp = FP_MODEL.create(data)
        return RM.success({"_id": fp})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesario enviar todos los parametros")

@bp.route('/delete/<string:id>', methods=['DELETE'])
def delete(id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")

@bp.route('/get_all', methods=['GET'])
def get_all(user_id):
    data = FP_MODEL.find_all(user_id)
    return RM.success(data)
