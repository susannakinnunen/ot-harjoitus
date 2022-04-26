import unittest
from repositories.stretch_repository import StretchRepository
from initialize_database import initialize_database

class Stretch(unittest.TestCase):
    def setUp(self):
        self.stretch_repository = StretchRepository()
        initialize_database

    def test_write_stretches_to_file_and_database(self):
        vastaus = self.stretch_repository.write_stretches_to_file_and_database("Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")

        self.assertEqual(vastaus,"Ranteen venytys ja Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")

    
    def test_get_stretches_from_file(self):
        self.stretch_repository.write_stretches_to_file_and_database("Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")
        vastaus = self.stretch_repository.get_stretches_from_file()
        
        self.assertEqual(vastaus,["Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle."])


    def find_all(self):
        self.stretch_repository.write_stretches_to_file_and_database("Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")
        vastaus = self.stretch_repository.find_all()

        self.assertEqual(vastaus, self.stretch_repository.write_stretches_to_file_and_database([("Ranteen venytys", "Nosta toinen käsivarsi suorana hieman ylöspäin etuvartalosi edessä. Paina toisella kädellä suorana olevan käden kämmenselkää kohti etuvartaloa. Sormet osoittavat kohti lattiaa. Käännä sitten venytettävän puolen kämmen pois päin etukehosta, sormet kohti lattiaa. Paina toisella kädellä venytettävän käden sormia kohti etukehoaa.Toista liikkeet myös toiselle puolelle.")]))