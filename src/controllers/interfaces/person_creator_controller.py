from abc import ABC, abstractmethod

class PersonCreatorControllersInterface(ABC):

    @abstractmethod
    def create(self, person_info: dict) -> dict:
        pass