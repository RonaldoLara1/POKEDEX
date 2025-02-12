from app import mongo
from app.models.superClase import SuperClase

class PokemonFavorites:
    def __init__(self):
        super().__init__("pokemon_favorites")