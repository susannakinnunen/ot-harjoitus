import unittest
from repositories.bodypart_repository import BodypartRepository
from repositories.stretch_repository import StretchRepository
from initialize_database import initialize_database
from entities.bodypart import Bodypart


class TestBodyparts(unittest.TestCase):
    def setUp(self):
        self.bodypart_repository = BodypartRepository()
        self.stretch_repository = StretchRepository()
        self.stretch_repository.delete_all()
        self.bodypart_repository.delete_all()
        initialize_database()

    def test_add_bodypart(self):
        vastaus = self.bodypart_repository.add_bodypart("niska")

        self.assertEqual(vastaus, "Lisätty kehonosa: niska")

    def test_write_bodyparts_to_file_and_database(self):
        vastaus = self.bodypart_repository.write_bodyparts_to_file_and_database(
            "ranne", "Ranteen venytys")

        self.assertEqual(
            vastaus, "Lisätty kehonosa ja venytys: ranne ja Ranteen venytys")

    def test_get_bodyparts_from_file(self):
        self.bodypart_repository.write_bodyparts_to_file_and_database(
            "ranne", "Ranteen venytys")
        vastaus = self.bodypart_repository.get_bodyparts_from_file()

        self.assertEqual(vastaus, ["ranne"])

    def test_find_all(self):
        self.bodypart_repository.add_bodypart("niska")

        vastaus = self.bodypart_repository.find_all()

        self.assertEqual(vastaus, ["niska"])
