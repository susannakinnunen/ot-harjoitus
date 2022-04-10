import unittest
import users
from initialize_database import initialize_database
import database_connection

class TestUser(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_registering(self):
        initialize_database()
        U = users.User(database_connection.get_database_connection())
        username = "testinimi"
        password = "testisalasana"
        vastaus =  U.add_user(username,password)

        self.assertEqual(vastaus, "Lisätty käyttäjätunnus testinimi ja salasana testisalasana")
