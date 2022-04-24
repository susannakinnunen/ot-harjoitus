from entities.bodypart import Bodypart
from database_connection import get_database_connection

class BodypartRepository:
    def __init__(self):
        self.connection = get_database_connection()

    def add_bodypart(self, name):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO Bodyparts (name) VALUES (:name)", {"name": name})

            self.connection.commit()

            return f"Lisätty kehonosa: {name}"
        
        except:
            return

    def find_all(self):
        cursor = self.connection.cursor()

        cursor.execute("SELECT name FROM Bodyparts")

        rows = cursor.fetchall()

        list = [row["name"] for row in rows]

        for bodypart in list:
            bodypart_object = Bodypart(bodypart)
            if bodypart_object not in list:
                list.remove(bodypart)
                list.append(bodypart_object)
        
        return list
    
    def get_bodyparts_from_file(self):
        with open("bodyparts.csv") as file:
            for row in file:
                row = row.replace("\n", "")
                bodypart = row.split(",")
                bodypart = bodypart[0]
                self.add_bodypart(bodypart)


    def get_bodypart_id(self,name):
        cursor = self.connection.cursor()
        result = cursor.execute(
            "SELECT id FROM Bodyparts WHERE name=:name", {"name": name})

        bodypart_id_result = result.fetchone()
        if bodypart_id_result is None:
            return False
        bodypart_id = bodypart_id_result[0]

        return bodypart_id
