import bodyparts
import database_connection


def find_stretch(bodypart_name):
    connection = database_connection.get_database_connection()
    cursor = connection.cursor()

    bodypart_id = bodyparts.get_bodypart_id(bodypart_name)
    stretch_id = get_stretch_id_by_id(bodypart_id)

    cursor.execute("SELECT S.name, S.description FROM Stretches S WHERE id=:stretch_id", {
                   "stretch_id": stretch_id})

    rows = cursor.fetchall()

    return [(row["name"], row["description"]) for row in rows]


def find_all():
    connection = database_connection.get_database_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Stretches")

    rows = cursor.fetchall()

    return [(row["name"], row["description"]) for row in rows]


def get_stretch_id_by_id(bodypart_id):
    connection = database_connection.get_database_connection()
    cursor = connection.cursor()

    result = cursor.execute("SELECT stretch_id FROM BodypartStretches" \
         "WHERE bodypart_id=:bodypart_id", {"bodypart_id": bodypart_id})
    stretch_id_result = result.fetchone()
    strech_id = stretch_id_result[0]
    return strech_id


def get_stretch_id_by_name(stretch_name):
    connection = database_connection.get_database_connection()
    cursor = connection.cursor()

    result = cursor.execute("SELECT id FROM Stretches WHERE name=:name", {
                            "name": stretch_name})
    stretch_id_result = result.fetchone()
    strech_id = stretch_id_result[0]
    return strech_id


class Stretch:
    def __init__(self, connection):
        self._connection = connection

    def add_stretch(self, name, description):
        cursor = self._connection.cursor()
        sql = "INSERT INTO Stretches (name, description) VALUES (:name, :description)"
        cursor.execute(sql, {"name": name, "description": description})
        self._connection.commit()
