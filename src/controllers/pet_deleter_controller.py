from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

class PetDeleterController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_reposotiry = pet_repository

    def delete(self, name:str) -> None:
        self.__pet_reposotiry.delete_pets(name)