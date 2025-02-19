from app import mongo
from app.models.superClase import SuperClase
from bson import ObjectId

class Pokemon(SuperClase):
    def __init__(self):
        super().__init__("pokemons")

        def find_by_id(self, object_id):
            raise NotImplementedError("El pokemon no se puede traer")
        
        def update(self, object_id, data):
            raise NotImplementedError("Los Pokemones No Se Pueden Actualizar")
        
        def find_all(self, user_id):
            data = self.collection.find({"user:id": ObjectId(user_id)})
            return data