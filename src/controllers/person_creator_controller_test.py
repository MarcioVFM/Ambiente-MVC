import pytest
from .person_creator_controller import PersonCreatorControllers

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int,pet_id: int) ->None: 
        pass

def test_creat_person():
    person_info = {
        'first_name': 'Fulano',
        'last_name': 'deTal',
        'age': 20,
        'pet_id': 22
    }

    controller = PersonCreatorControllers(MockPeopleRepository())
    response = controller.create(person_info)

    assert response['data']['type'] == 'Person'
    assert response['data']['count'] == 1
    assert response['data']['attributes'] == person_info

def test_creat_person_error():
    person_info = {
        'first_name': 'Fulano123',
        'last_name': 'deTal',
        'age': 20,
        'pet_id': 22
    }

    controller = PersonCreatorControllers(MockPeopleRepository())

    with pytest.raises(Exception):
        controller.create(person_info)
