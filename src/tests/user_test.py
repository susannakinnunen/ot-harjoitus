import unittest
from initialize_database import initialize_database
from repositories.user_repository import UserRepository


class TestUser(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.user_repository = UserRepository()
        self.username = "testinimi"
        self.password = "testisalasana"

    def test_registering(self):
        vastaus = self.user_repository.add_user(self.username, self.password)
        self.assertEqual(
            vastaus, "Lisätty käyttäjätunnus testinimi ja salasana testisalasana")

    def test_login_correct(self):
        self.user_repository.add_user(self.username, self.password)
        vastaus = self.user_repository.login(self.username, self.password)

        self.assertEqual(vastaus, True)

    def test_login_incorrect_username(self):
        self.user_repository.add_user(self.username, self.password)
        vastaus = self.user_repository.login("vääränimi", self.password)

        self.assertEqual(vastaus, False)

    def test_login_incorrect_password(self):
        self.user_repository.add_user(self.username, self.password)
        vastaus = self.user_repository.login(self.username, "vääräsalasana")

        self.assertEqual(vastaus, False)
