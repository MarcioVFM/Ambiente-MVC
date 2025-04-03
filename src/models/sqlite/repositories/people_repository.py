class PeopleRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection