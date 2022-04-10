import unittest
import users
from initialize_database import initialize_database
import database_connection

class TestUser(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.U = users.User(database_connection.get_database_connection())
        self.username = "testinimi"
        self.password = "testisalasana"

    def test_registering(self):
        vastaus =  self.U.add_user(self.username,self.password)
        self.assertEqual(vastaus, "Lisätty käyttäjätunnus testinimi ja salasana testisalasana")


    def test_login_correct(self):
        self.U.add_user(self.username,self.password)
        vastaus =  self.U.login(self.username,self.password)

        self.assertEqual(vastaus, True)

    def test_login_incorrect_username(self):
        self.U.add_user(self.username,self.password)
        vastaus =  self.U.login("vääränimi",self.password)

        self.assertEqual(vastaus, False)

    def test_login_incorrect_password(self):
        self.U.add_user(self.username,self.password)
        vastaus =  self.U.login(self.username,"vääräsalasana")

        self.assertEqual(vastaus, False) 

