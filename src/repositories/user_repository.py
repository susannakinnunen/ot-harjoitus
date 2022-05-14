from database_connection import get_database_connection

# pylint disable "except"-kohdissa, sillä tämä on ainoa tapa,
# jolla osaan toteuttaa sql-toiminnot virhetilanteissa


class UserRepository:
    """ Käyttäjiin liittyvistä operaatioista vastaava luokka.
    """

    def __init__(self):
        self._connection = get_database_connection()

    def add_user(self, username, password, admin):
        """Lisää käyttäjänimen, salasanan ja admin-arvon tietokantaan"""
        cursor = self._connection.cursor()

        if admin is True:
            try:
                cursor.execute(
                    "INSERT INTO Users (username,password, is_admin) VALUES "
                    "(:username, :password, True)", {
                        "username": username, "password": password})

                self._connection.commit()

                return f"Lisätty käyttäjätunnus {username} ja salasana {password}"
            except: # pylint: disable=bare-except
                return False
        try:
            cursor.execute(
                "INSERT INTO Users (username,password, is_admin) "
                "VALUES (:username, :password, False)", {
                    "username": username, "password": password})

            self._connection.commit()

            return f"Lisätty käyttäjätunnus {username} ja salasana {password}"
        except: # pylint: disable=bare-except
            return False

    def login(self, username, password):
        """Kirjaa käyttäjän sisään, jos käytttäjätunnus on oikein ja olemassa."""
        user = self.find_by_username(username)

        if user is None or user[1] != password:
            return False

        return True

    def find_by_username(self, username):
        """Etsii käyttäjän käyttäjänimen perusteella"""
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Users WHERE username=:username", {"username": username})

        row = cursor.fetchone()

        if row is None:
            return None

        return row['username'], row['password']
