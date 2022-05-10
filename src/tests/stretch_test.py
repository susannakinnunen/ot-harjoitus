import unittest
from repositories.stretch_repository import StretchRepository
from repositories.bodypart_stretch_repository import BodypartStretchRepository
from repositories.bodypart_repository import BodypartRepository
from initialize_database import initialize_database


class Stretch(unittest.TestCase):
    def setUp(self):
        self.stretch_repository = StretchRepository()
        self.bodypart_stretch_repository = BodypartStretchRepository()
        self.bodypart_repository = BodypartRepository()
        self.stretch_repository.delete_all()
        self.bodypart_repository.delete_all()
        initialize_database()

    def test_write_stretches_to_file_and_database(self):
        vastaus = self.stretch_repository.write_stretches_to_file_and_database(
            "Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")

        self.assertEqual(vastaus, "Ranteen venytys ja Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")

    def test_get_stretches_from_file(self):
        self.stretch_repository.write_stretches_to_file_and_database(
            "Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")
        vastaus = self.stretch_repository.get_stretches_from_file()

        self.assertEqual(vastaus, ["Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle."])

    def test_find_all(self):
        self.stretch_repository.write_stretches_to_file_and_database(
            "Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")
        vastaus = self.stretch_repository.find_all()

        self.assertEqual(vastaus, [("Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")])
    """
    def test_find_by_bodypart(self):
        self.stretch_repository.write_stretches_to_file_and_database(
            "Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")

        self.bodypart_repository.add_bodypart("ranne")

        self.bodypart_stretch_repository.add_combination("ranne", "Ranteen venytys")

        vastaus = self.stretch_repository.find_by_bodypart("ranne")

        self.assertEqual(vastaus, [("Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")])
    """

    def test_find_by_bodypart_false_bodypart_id(self):
        vastaus = self.stretch_repository.find_by_bodypart("ranne")
        self.assertEqual(vastaus, False)

    def test_find_by_bodypart_false_stretch_id(self):
        self.bodypart_repository.add_bodypart("ranne")
        vastaus = self.stretch_repository.find_by_bodypart("ranne")
        self.assertEqual(vastaus, False)

    def test_get_stretch_id_by_id(self):
        self.stretch_repository.write_stretches_to_file_and_database(
            "Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")

        self.bodypart_repository.add_bodypart("ranne")

        self.bodypart_stretch_repository.add_combination(
            "ranne", "Ranteen venytys")

        bodypart_id = self.bodypart_repository.get_bodypart_id("ranne")

        vastaus = self.stretch_repository.get_stretch_id_by_id(bodypart_id)

        self.assertEqual(vastaus, 1)
