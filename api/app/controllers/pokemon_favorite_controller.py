from flask import Blueprint, request, jsonify
from app.models.factory import ModelFactory
from bson import ObjectId
from marshmallow import ValidationError
from app.schemas.user_schema import UserSchema 
from app.tools.response_manager import ResponseManager
from app.schemas.pokemon_favorites_schema import FavoriteSchema
from flask_jwt_extended import jwt_required,get_jwt_identity

RM = ResponseManager()
bp = Blueprint('pokemon_favorites', __name__, url_prefix='/favorite-pokemons')
FP_MODEL = ModelFactory.get_model("pokemon_favorites")
FP_SCHEMA = FavoriteSchema()


@bp.route('/', methods=['POST'])
@jwt_required()
def create():
    user_id = get_jwt_identity()
    try:
        data = request.json
        data= FP_SCHEMA.load(data)
        data["user_id"] = user_id
        fp = FP_MODEL.create(data)
        return RM.success({"_id": fp})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesario enviar todos los parametros")

@bp.route('/delete/<string:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")

@bp.route('/get_all', methods=['GET'])
@jwt_required()
def get_all():
    user_id = get_jwt_identity()
    data = FP_MODEL.find_all(user_id)
    return RM.success(data)
