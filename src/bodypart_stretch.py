import bodyparts
import stretches


class BodypartStretch:
    def __init__(self, connection):
        self._connection = connection

    def add_combination(self, bodypart_name, stretch_name):
        cursor = self._connection.cursor()

        bodypart_id = bodyparts.get_bodypart_id(bodypart_name)
        stretch_id = stretches.get_stretch_id_by_name(stretch_name)

        cursor.execute("INSERT INTO BodypartStretches (stretch_id, bodypart_id)" \
        "VALUES (:stretch_id, :bodypart_id)", \
        {"stretch_id": stretch_id, "bodypart_id": bodypart_id})

        self._connection.commit()
