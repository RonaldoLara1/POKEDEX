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


@bp.route('/get_all', methods=['GET'])
def get_all(pokemon_id):
    data = FP_MODEL.find_all(pokemon_id)
    return RM.success(data)

@bp.route('/get_one', methods=['GET'])
def get_by_id(pokemon_id):
    data = FP_MODEL.find_by_id(pokemon_id)
    return RM.success(data)
