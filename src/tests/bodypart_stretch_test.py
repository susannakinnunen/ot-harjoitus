import unittest
from repositories.bodypart_stretch_repository import BodypartStretchRepository
from repositories.bodypart_repository import BodypartRepository
from repositories.stretch_repository import StretchRepository
from initialize_database import initialize_database


class TestBodypartStretch(unittest.TestCase):
    def setUp(self):
        self.bodypart_stretch_repository = BodypartStretchRepository()
        self.bodypart_repository = BodypartRepository()
        self.stretch_repository = StretchRepository()
        self.bodypart_repository.delete_all()
        self.stretch_repository.delete_all()
        initialize_database

    def test_get_bodyparts_and_stretches_from_file(self):
        self.bodypart_repository.write_bodyparts_to_file_and_database(
            "ranne", "Ranteen venytys")
        vastaus = self.bodypart_stretch_repository.get_bodyparts_and_stretches_from_file()
        self.assertEqual(vastaus, "ranne ja Ranteen venytys")
