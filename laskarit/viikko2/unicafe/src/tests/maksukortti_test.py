import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(400)
        
        self.assertEqual(str(self.maksukortti), "saldo: 4.1")

    def test_rahan_ottaminen_toimii_kun_rahaa_tarpeksi(self):
        self.maksukortti.lataa_rahaa(400)
        self.maksukortti.ota_rahaa(400)

        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldo_ei_muutu_kun_rahaa_liian_vähän(self):
        self.maksukortti.ota_rahaa(400)

        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

