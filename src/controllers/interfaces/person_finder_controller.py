from abc import ABC, abstractmethod

class PersonFinderControllersInterface(ABC):

    @abstractmethod
    def find(self, person_id: int) -> dict:
        pass