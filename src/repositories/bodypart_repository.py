from entities.bodypart import Bodypart
from database_connection import get_database_connection
from config import bodypart_file

# pylint disable rivillä 102,
# sillä funktio poistaa tiedostosta kaiken datan, ja tarvitsen tällaista toimintoa.
# pylint disable myös "except"-kohdissa, en osannut vielä korjata niitä


class BodypartRepository:
    """Kehonosiin iittyvistä tietokantaoperaatioista ja csv-tiedosto-operaatioista vastaava luokka.
    """

    def __init__(self):
        self.connection = get_database_connection()

    def add_bodypart(self, name):
        cursor = self.connection.cursor()
        try:
            check = self.check_if_exists(name)
            if check is True:
                return True

            cursor.execute(
                "INSERT INTO Bodyparts (name) VALUES (:name)", {"name": name})

            self.connection.commit()

            return f"Lisätty kehonosa: {name}"

        except:  # pylint: disable=bare-except
            return False

    def check_if_exists(self, name):
        cursor = self.connection.cursor()

        sql = cursor.execute(
            "SELECT name FROM Bodyparts WHERE name=:name", {"name": name})
        result = sql.fetchone()
        if result is None:
            return False
        return True

    def find_all(self):
        cursor = self.connection.cursor()

        cursor.execute("SELECT name FROM Bodyparts")

        rows = cursor.fetchall()

        lista = [row["name"] for row in rows]
        for bodypart in lista:
            bodypart_object = Bodypart(bodypart)
            if bodypart_object not in lista:
                lista.remove(bodypart)
                lista.append(str(bodypart_object))

        return lista

    def get_bodyparts_from_file(self):
        bodypart_list = []
        with open(bodypart_file, encoding='utf-8') as file:
            for row in file:
                row = row.replace("\n", "")
                bodypart = row.split(";")
                bodypart = bodypart[0]
                bodypart_list.append(bodypart)
        return bodypart_list

    def write_bodyparts_to_file_and_database(self, bodypart, stretch):
        """ Lisää kehonosan ja siihen kuuluvan venytyksen nimen
        bodyparts.csv-tiedostoon, kutsuu add_bodypart()-funktiota. """
        try:
            self.add_bodypart(bodypart)

            with open(bodypart_file, "a", encoding='utf-8') as file:
                file.write(bodypart+";"+stretch+"\n")
            return f"Lisätty kehonosa ja venytys: {bodypart} ja {stretch}"

        except:  # pylint: disable=bare-except
            return False

    def get_bodypart_id(self, name):
        cursor = self.connection.cursor()
        result = cursor.execute(
            "SELECT id FROM Bodyparts WHERE name=:name", {"name": name})

        bodypart_id_result = result.fetchone()
        if bodypart_id_result is None:
            return False
        bodypart_id = bodypart_id_result[0]

        return bodypart_id

    def delete_all(self):
        with open(bodypart_file, "w", encoding='utf-8') as file:  # pylint: disable=unused-variable
            pass
