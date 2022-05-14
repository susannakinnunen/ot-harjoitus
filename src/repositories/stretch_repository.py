from database_connection import get_database_connection
from repositories.bodypart_repository import BodypartRepository
from config import stretch_file

# pylint disable rivillä 106,
# sillä funktio poistaa tiedostosta kaiken datan, ja tarvitsen tällaista toimintoa.
# pylint disable myös "except"-kohdissa, sillä tämä on ainoa tapa,
# jolla osaan toteuttaa sql-toiminnot virhetilanteissa


class StretchRepository():
    """ Venytysten tallentamisesta ja muokkaamisesta vastaava luokka.
    """

    def __init__(self):
        self.connection = get_database_connection()
        self.bodypart_repository = BodypartRepository()

    def get_stretches_from_file(self):
        """Hakee venytysten nimet ja ohjeet stretches.csv-tiedostosta.
        Vie venytykset tallennettavaksi add_stretch-metodille"""
        stretch_list = []
        with open(stretch_file, encoding='utf-8') as file:
            for row in file:
                row = row.replace("\n", "")
                row = row.split(";")
                stretch_name = row[0]
                stretch_description = row[1]
                stretch_list.append(stretch_name)
                stretch_list.append(stretch_description)
                self.add_stretch(stretch_name, stretch_description)
        return stretch_list

    def add_stretch(self, name, description):
        """Lisää venytykset ja niiden ohjeet tietokantaan"""
        cursor = self.connection.cursor()
        try:
            sql = "INSERT INTO Stretches (name, description) VALUES (:name, :description)"

            cursor.execute(sql, {"name": name, "description": description})

            self.connection.commit()
            return True
        except: # pylint: disable=bare-except
            return False

    def write_stretches_to_file_and_database(self, name, description):
        """Lisää venytyksen stretches.csv-tiedostoon ja
         ohjaa ne lisättäväksi tietokantaan"""
        try:
            self.add_stretch(name, description)

            with open(stretch_file, "a", encoding='utf-8') as file:
                file.write(name+";"+description+"\n")

            return f"{name} ja {description}"
        except:  # pylint: disable=bare-except
            return False

    def find_all(self):
        """Hakee kaikki venytykset tietokannasta"""
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM Stretches")

        rows = cursor.fetchall()

        return [(row["name"], row["description"]) for row in rows]

    def find_by_bodypart(self, bodypart):
        """Hakee venytyksen nimen ja ohjeen kehonosan perusteella"""
        cursor = self.connection.cursor()
        stretch_list = []
        bodypart_id = self.bodypart_repository.get_bodypart_id(bodypart)
        if bodypart_id is False:
            return False
        stretch_ids = self.get_stretch_id_by_id(bodypart_id)
        if stretch_ids is False:
            return False

        for stretch_id in stretch_ids:
            cursor.execute("SELECT S.name, S.description FROM Stretches S WHERE id=:stretch_id", {
                "stretch_id": stretch_id})

            rows = cursor.fetchall()
            for row in rows:
                row_item = (row["name"], row["description"])
                stretch_list.append(row_item)
        return stretch_list

    def get_stretch_id_by_id(self, bodypart_id):
        """Hakee venytyksetn id:n kehonosa id:n perusteella."""
        cursor = self.connection.cursor()
        result = cursor.execute("SELECT stretch_id FROM BodypartStretches "
                                "WHERE bodypart_id=:bodypart_id",{
                                "bodypart_id": bodypart_id})
        stretch_id_results = result.fetchall()
        if stretch_id_results is None or stretch_id_results == []:
            return False
        return [stretch_id_result["stretch_id"] for stretch_id_result in stretch_id_results]

    def get_stretch_id_by_name(self, stretch_name):
        """Hakee venytyksen id:n venytyksetn nimen perusteella"""
        cursor = self.connection.cursor()

        result = cursor.execute("SELECT id FROM Stretches WHERE name= :name",
                                {"name": stretch_name})
        stretch_id_result = result.fetchone()
        if stretch_id_result is None:
            return False

        strech_id = stretch_id_result[0]
        return strech_id

    def delete_all(self):
        """Poistaa kaikki stretches.csv-tiedostosta"""
        with open(stretch_file, "w", encoding='utf-8') as file:  # pylint: disable=unused-variable
            pass
