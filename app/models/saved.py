from app import mongo

class PokemonSaved:
    collection = mongo.db.pokemon_saved

    @staticmethod
    def find_all():
        pokemon_saved = PokemonSaved.collection.find()
        return list(pokemon_saved)

    @staticmethod
    def find_by_id(saved_id):
        pokemon = PokemonSaved.collection.find_one({
            "_id": saved_id
        })
        return pokemon

    @staticmethod
    def create(data):
        saved_pokemon = PokemonSaved.collection.insert_one(data)
        return saved_pokemon.inserted_id

    @staticmethod
    def update(saved_id, data):
        pokemon = PokemonSaved.collection.update_one({
            "_id": saved_id
        }, {
            "$set": data
        })
        return pokemon.modified_count

    @staticmethod
    def delete(saved_id):
        return PokemonSaved.collection.delete_one({
            "_id": saved_id
        })
