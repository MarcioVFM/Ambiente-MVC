from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable

class PetListerController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def pets_list(self) -> dict:
        pets = self.__get_pets_in_db()
        response = self.__formatted_response(pets)
        return response

    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __formatted_response(self, pets: list[PetsTable]) -> dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({'name': pet.name, 'id': pet.id})

        return {
            'data': {
                'type': 'Pets',
                'count': len(formatted_pets),
                'attributes': formatted_pets
            }
        }
