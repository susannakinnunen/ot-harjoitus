from database_connection import get_database_connection
from repositories.bodypart_repository import BodypartRepository
from config import stretch_file

class StretchRepository():
    def __init__(self):
        self.connection = get_database_connection()
        self.bodypart_repository = BodypartRepository()

    def get_stretches_from_file(self):
        stretch_list = []
        with open(stretch_file) as file:
            for row in file:
                row = row.replace("\n", "")
                row = row.split(";")
                stretch_name = row[0]
                stretch_description = row[1]
                stretch_list.append(stretch_name)
                stretch_list.append(stretch_description)
                self.add_stretch(stretch_name,stretch_description)
        return stretch_list
    
    def add_stretch(self, name, description):
        cursor = self.connection.cursor()
        
        sql = "INSERT INTO Stretches (name, description) VALUES (:name, :description)"
        
        cursor.execute(sql, {"name": name, "description": description})
        
        self.connection.commit()

    def write_stretches_to_file_and_database(self, name, description):
        try:
            self.add_stretch(name,description)

            with open(stretch_file, "a") as file:
                file.write(name+";"+description+"\n")

            return f"{name} ja {description}"
        except:
            return False


    def find_all(self):
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM Stretches")

        rows = cursor.fetchall()

        return [(row["name"], row["description"]) for row in rows]

    def find_by_bodypart(self,bodypart):
        cursor = self.connection.cursor()

        bodypart_id = self.bodypart_repository.get_bodypart_id(bodypart)
        if bodypart_id == False:
            return False
        stretch_id = self.get_stretch_id_by_id(bodypart_id)
        if stretch_id == False:
            return False

        cursor.execute("SELECT S.name, S.description FROM Stretches S WHERE id=:stretch_id", {
                    "stretch_id": stretch_id})

        rows = cursor.fetchall()

        return [(row["name"], row["description"]) for row in rows]

    def get_stretch_id_by_id(self,bodypart_id):
        cursor = self.connection.cursor()
        result = cursor.execute("SELECT stretch_id FROM BodypartStretches WHERE bodypart_id=:bodypart_id", {
                                "bodypart_id": bodypart_id})
        stretch_id_result = result.fetchone()
        if stretch_id_result is None:
            return False

        strech_id = stretch_id_result[0]
        return strech_id


    def get_stretch_id_by_name(self,stretch_name):
        cursor = self.connection.cursor()

        result = cursor.execute("SELECT id FROM Stretches WHERE name= :name",
                                {"name": stretch_name})
        stretch_id_result = result.fetchone()
        if stretch_id_result is None:
            return False

        strech_id = stretch_id_result[0]
        return strech_id

    def delete_all(self):
        with open(stretch_file, "w") as file:
            pass
