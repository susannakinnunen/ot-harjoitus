from initialize_database import initialize_database
import database_connection

def find_all():
    connection = database_connection.get_database_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM Bodyparts")

    rows = cursor.fetchall()

    return [row["name"] for row in rows]

    
def get_bodypart_id(name):
    connection = database_connection.get_database_connection()
    cursor = connection.cursor()

    result = cursor.execute("SELECT id FROM Bodyparts WHERE name=:name", {"name":name})
    
    bodypart_id_result = result.fetchone()

    bodypart_id = bodypart_id_result[0]

    return bodypart_id




class Bodypart:
    def __init__(self, connection):
        self._connection = connection

    def add_bodypart(self, name):
        self.name = name

        cursor =  self._connection.cursor()

        cursor.execute("INSERT INTO Bodyparts (name) VALUES (:name)",{"name":name})

        self._connection.commit()

        return f"Lisätty kehonosa: {self.name}"