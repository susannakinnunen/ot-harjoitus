import unittest
from repositories.bodypart_repository import BodypartRepository
from initialize_database import initialize_database


class TestBodyparts(unittest.TestCase):
    def setUp(self):
        self.bodypart_repository = BodypartRepository()
        initialize_database()

    def test_add_bodypart(self):
        vastaus = self.bodypart_repository.add_bodypart("niska")

        self.assertEqual(vastaus, "Lisätty kehonosa: niska")
