from entities.bodypart import Bodypart
from database_connection import get_database_connection
from config import bodypart_file

class BodypartRepository:
    def __init__(self):
        self.connection = get_database_connection()

    def add_bodypart(self, name):
        cursor = self.connection.cursor()
        try:
            check = self.check_if_exists(name)
            if check:
                return "exists"
            else: 
                cursor.execute(
                    "INSERT INTO Bodyparts (name) VALUES (:name)", {"name": name})

                self.connection.commit()

                return f"Lisätty kehonosa: {name}"
            
        except:
            return False

    def check_if_exists(self,name):
        cursor = self.connection.cursor()

        sql = cursor.execute("SELECT name FROM Bodyparts WHERE name=:name", {"name": name})
        result = sql.fetchone()
        if result is None:
            return False
        else:
            return True


    def find_all(self):
        cursor = self.connection.cursor()

        cursor.execute("SELECT name FROM Bodyparts")

        rows = cursor.fetchall()

        list = [row["name"] for row in rows]
        for bodypart in list:
            bodypart_object = Bodypart(bodypart)
            if bodypart_object not in list:
                list.remove(bodypart)
                list.append(str(bodypart_object))
        
        return list
    
    def get_bodyparts_from_file(self):
        bodypart_list = []
        with open(bodypart_file) as file:
            for row in file:
                row = row.replace("\n", "")
                bodypart = row.split(";")
                bodypart = bodypart[0]
                bodypart_list.append(bodypart)
        return bodypart_list

    def add_stretchnames_to_bodyparts_file(self,bodypart_name,stretch_name):
        with open(bodypart_file, "w") as file:
            for row in file:
                row = row.replace("\n", "")
                bodypart_stretch_row = row.split(";")
                bodypart = bodypart_stretch_row[0]
                if bodypart == bodypart_name:
                    file.writerow(row+stretch_name+"\n")


    def write_bodyparts_to_file_and_database(self, bodypart, stretch):
        try:
            check = self.add_bodypart(bodypart)
            if check != "exists":
                with open(bodypart_file, "a") as file:
                    file.write(bodypart+";"+stretch+"\n")

                return f"Lisätty kehonosa ja venytys: {bodypart} ja {stretch}"
            else: 
                self.add_stretchnames_to_bodyparts_file(bodypart,stretch)
                

        except:
            return False



    def get_bodypart_id(self,name):
        cursor = self.connection.cursor()
        result = cursor.execute(
            "SELECT id FROM Bodyparts WHERE name=:name", {"name": name})

        bodypart_id_result = result.fetchone()
        if bodypart_id_result is None:
            return False
        bodypart_id = bodypart_id_result[0]

        return bodypart_id

    
    def delete_all(self):
        with open(bodypart_file, "w") as file:
            pass
        
