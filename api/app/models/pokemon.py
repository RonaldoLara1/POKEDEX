from app import mongo
from app.models.superClase import SuperClase

class Pokemon(SuperClase):
    def __init__(self):
        super().__init__("pokemons")

        def create(self, data):
            raise NotImplementedError("Los Pokemones No Se Pueden Crear")
        
        def delete(self, object_id):
            raise NotImplementedError("Los Pokemones No Se Pueden Eliminar")
        
        def update(self, object_id, data):
            raise NotImplementedError("Los Pokemones No Se Pueden Actualizar")