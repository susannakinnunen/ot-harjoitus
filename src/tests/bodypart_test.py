import unittest
import bodyparts
from initialize_database import initialize_database
import database_connection

class TestBodyparts(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
    
    def test_add_bodypart(self):
        initialize_database()
        B = bodyparts.Bodypart(database_connection.get_database_connection())
        vastaus = B.add_bodypart("niska")
        
        self.assertEqual(vastaus,"Lisätty kehonosa: niska")