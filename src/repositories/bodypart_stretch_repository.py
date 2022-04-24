from database_connection import get_database_connection
from repositories.bodypart_repository import BodypartRepository
from repositories.stretch_repository import StretchRepository

class BodypartStretchRepository():
    def __init__(self):
        self.connection = get_database_connection()
        self.bodypart_repository = BodypartRepository()
        self.stretch_repository = StretchRepository()

    def get_bodyparts_and_stretches_from_file(self):
        with open("bodyparts.csv") as file:
            for row in file:
                row = row.replace("\n", "")
                list = row.split(",")
                bodypart = list[0]
                for stretch in list:
                    if stretch == list[0]:
                        continue
                    self.add_combination(bodypart,stretch)


    def add_combination(self, bodypart_name, stretch_name):

        cursor = self.connection.cursor()

        bodypart_id = self.bodypart_repository.get_bodypart_id(bodypart_name)
        stretch_id = self.stretch_repository.get_stretch_id_by_name(stretch_name)

        cursor.execute("INSERT INTO BodypartStretches (stretch_id, bodypart_id)"
                       "VALUES (:stretch_id, :bodypart_id)",
                       {"stretch_id": stretch_id, "bodypart_id": bodypart_id})

        self.connection.commit()

