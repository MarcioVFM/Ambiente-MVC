from abc import ABC, abstractmethod

class PetListerControllerInterface(ABC):

    @abstractmethod
    def pets_list(self) -> dict:
        pass