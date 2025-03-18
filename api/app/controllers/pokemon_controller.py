from flask import Blueprint, request, jsonify
from app.models.factory import ModelFactory
from bson import ObjectId
from marshmallow import ValidationError
from app.schemas.user_schema import UserSchema 
from app.tools.response_manager import ResponseManager
from app.schemas.pokemon_favorites_schema import FavoriteSchema
from flask_jwt_extended import jwt_required

RM = ResponseManager()
bp = Blueprint('user_controller', __name__, url_prefix='/pokemon')
PM = ModelFactory.get_model("pokemons")


@bp.route('/', methods=['GET'])
@jwt_required()
def get_all():
    data = PM.find_all()
    return RM.success(data)

@bp.route('/get/<string:pokemon_id>', methods=['GET'])
@jwt_required()
def get_pokemon(pokemon_id):
    data = PM.find_one(ObjectId (pokemon_id))
    return RM.success(data)
