from repositories.bodypart_repository import BodypartRepository
from repositories.stretch_repository import StretchRepository
from repositories.bodypart_stretch_repository import BodypartStretchRepository
from repositories.user_repository import UserRepository


class StretchingService:
    """ Sovelluslogiikasta vastaava luokka
    """

    def __init__(self):
        self.bodypart_repository = BodypartRepository()
        self.stretch_repository = StretchRepository()
        self.bodypart_stretch_repository = BodypartStretchRepository()
        self.user_repository = UserRepository()

    def add_bodypart(self, name, stretch):
        """ Kutsuu BodypartRepository-luokkaa tallentamaan kehonsa- ja venytystietoja csv.tiedostoon ja tietokantaan. """
        return self.bodypart_repository.write_bodyparts_to_file_and_database(
            name, stretch)

    def add_stretch(self, bodypart_name, description):
        """ Kutsuu StretchRepository-luokkaa tallentamaan kehonsa- ja venytystietoja csv.tiedostoon ja tietokantaan. """
        return self.stretch_repository.write_stretches_to_file_and_database(
            bodypart_name, description)

    def add_combination(self, name, stretch):
        """ Kutsuu BodypartStretch-luokkaa lisäämään yhdistämään tietokannassa tietyn kehonosan ja venytyksen id:t"""
        return self.bodypart_stretch_repository.add_combination(name, stretch)

    def get_all_bodyparts(self):
        """ Kutsuu BodypartRepositiry-luokkaa hakemaan kaikki kehonosat"""
        return self.bodypart_repository.find_all()

    def show_stretch(self, bodypart):
        """ Kutsuu StretchRepository-luokkaa hakemaan venytyksen tietyn kehonosan perusteella"""
        return self.stretch_repository.find_by_bodypart(bodypart)

    def combine_stretches_and_bodyparts(self):
        """ Kutsuu BodypartRepository-luokkaa yhdistämään venytyksen ja kehonosan csv.tiedostosta tietokantaan. Tehdään ohjelman käynnistyksen yhteydessä. """
        self.bodypart_stretch_repository.get_bodyparts_and_stretches_from_file()

    def create_new_user(self, username, password):
        """ Kutsuu UserRpository-luokkaa luomaan uuden käyttäjätunnuksen. Tarkistaa onko käyttäjä ylläpitäjä. Palauttaa tiedon siitä, onko käyttäjätunnus jo olemassa, jolloin käyttäjätunnusta ei voi luoda. Jos sitä ei voi luoda, palauttaa False."""
        admin = self.check_if_admin(username)
        user = self.user_repository.add_user(username, password, admin)
        if not user:
            return False
        return True

    def login(self, username, password):
        """ Kutsuu UserRepository-luokkaa kirjautumaan sisään tietyllä käyttäjätunnuksella ja salasanalla. """
        login = self.user_repository.login(username, password)
        return login

    def check_if_admin(self, username):
        """Tarkistaa onko käyttäjä ylläpitäjä. Luokan sisäinen metodi."""
        if username == "admin":
            return True
        else:
            return False
