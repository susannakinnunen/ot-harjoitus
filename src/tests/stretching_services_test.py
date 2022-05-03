import unittest
from initialize_database import initialize_database
from services.stretching_services import StretchingService
from repositories.bodypart_repository import BodypartRepository
from repositories.stretch_repository import StretchRepository

class TestStretchingService(unittest.TestCase):
    def setUp(self):
        self.stretching_service = StretchingService()
        self.stretch_repository = StretchRepository()
        self.bodypart_repository = BodypartRepository()
        self.stretch_repository.delete_all()
        self.bodypart_repository.delete_all()
        initialize_database()
    
    def test_check_if_admin_true(self):
        admin = "admin"
        vastaus = self.stretching_service.check_if_admin(admin)

        self.assertEqual(
            vastaus, True)

    def test_check_if_admin_false(self):
        admin = "user"
        vastaus = self.stretching_service.check_if_admin(admin)

        self.assertEqual(
            vastaus, False)    

    def test_add_bodypart(self):
            bodypart = "ranne"
            stretch = "Ranteen venytys"
            vastaus = self.stretching_service.add_bodypart(bodypart, stretch)
            self.assertEqual(vastaus, f"Lisätty kehonosa ja venytys: {bodypart} ja {stretch}")

    def test_add_stretch(self):
        stretch_name =  "Ranteen venytys" 
        description = "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle."
        vastaus = self.stretching_service.add_stretch(stretch_name,description)

        self.assertEqual(vastaus, f"{stretch_name} ja {description}")

    def test_add_combination(self):
        bodypart_name = "ranne"
        stretch_name = "Eteenpäintaivutus"

        self.stretch_repository.write_stretches_to_file_and_database(
            "Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")
        
        self.bodypart_repository.add_bodypart("ranne")

        vastaus = self.stretching_service.add_combination(bodypart_name,stretch_name)

        self.assertEqual(vastaus, f"Lisätty {bodypart_name} ja {stretch_name}")

