from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInteface
import re

class PersonCreatorControllers:
    def __init__(self,people_repository: PeopleRepositoryInteface) -> None:
        self.__people_repository = people_repository

    def create(self, person_info: dict) -> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_first_and_last_name(first_name, last_name)
        

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        #expressao regular para caracteres que nao sao letras
        non_valid_caracteres = re.compile(r'[^a-zA-Z]')

        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
            raise Exception('Nome da pessoa invalido!')