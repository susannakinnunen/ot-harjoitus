import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_alku_asetus_oikein(self):
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100000, ostetut edulliset: 0, ostetut maukkaat: 0")

    def test_vaihtoraha_oikea_kateisella_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihtoraha, 10)


    def test_vaihtoraha_oikea_kateisella_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(vaihtoraha, 10)

    def test_kassan_rahamaara_ja_myyntimaara_kasvaa_edullisen_verran(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100240, ostetut edulliset: 1, ostetut maukkaat: 0")

    def test_kassan_rahamaara_ja_myyntimaara_kasvaa_maukkaan_verran(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100400, ostetut edulliset: 0, ostetut maukkaat: 1")

    def test_maksu_ei_riittava_edulliseen_kateisella(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(palautus, 200)

    def test_maksu_ei_riittava_maukkaaseen_kateisella(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(palautus, 300)

    def test_myyntimaara_ei_lisaanny_edullinen_kateisella_rahat_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100000, ostetut edulliset: 0, ostetut maukkaat: 0")

    def test_myyntimaara_ei_lisaanny_maukas_kateisella_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100000, ostetut edulliset: 0, ostetut maukkaat: 0")

    
    def test_myyntimaara_edullinen(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100000, ostetut edulliset: 1, ostetut maukkaat: 0")

    def test_myyntimaara_maukas(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100000, ostetut edulliset: 0, ostetut maukkaat: 1")


    def test_kortin_saldo_edullinen(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 0.0")

    def test_kortin_saldo_maukas(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 0.0")

    def test_kortin_saldo_ei_riita_edullinen(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 2.0")

    
    def test_kortin_saldo_ei_riita_maukas(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 3.0")

    
    def test_myyntimaara_ei_lisaanny_edullinen_kortilla_rahat_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100000, ostetut edulliset: 0, ostetut maukkaat: 0")

    def test_myyntimaara_ei_lisaanny_maukas_kortilla_rahat_ei_riita(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100000, ostetut edulliset: 0, ostetut maukkaat: 0")

    def test_kortille_ladattaessa_kortin_uusi_saldo(self):
        kortti = Maksukortti(0)
        summa = 500
        self.kassapaate.lataa_rahaa_kortille(kortti,summa)
        self.assertEqual(str(kortti), "saldo: 5.0")

    def test_kortille_ladattaessa_kassan_uusi_rahamaara(self):
        kortti = Maksukortti(0)
        summa = 500
        self.kassapaate.lataa_rahaa_kortille(kortti,summa)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100500, ostetut edulliset: 0, ostetut maukkaat: 0")
    

    def test_kortille_ladataan_negatiivinen_summa(self):
        kortti = Maksukortti(0)
        summa = -100
        self.kassapaate.lataa_rahaa_kortille(kortti,summa)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa: 100000, ostetut edulliset: 0, ostetut maukkaat: 0")
    
    
    


    