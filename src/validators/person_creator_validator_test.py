from .person_creator_validator import person_creator_validator

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body

def test_person_creator_validaor():
    request = MockRequest({
        'first_name': 'fulano',
        'last_name': 'de tal',
        'age': 20,
        'pet_id': 4
    })

    person_creator_validator(request)