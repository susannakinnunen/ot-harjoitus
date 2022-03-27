import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
	def setUp(self):
		self.kortti = Maksukortti(10)

	def test_konstruktori_asettaa_saldon_oikein(self):

        	vastaus = str(self.kortti)

        	self.assertEqual(vastaus, "Kortilla on rahaa 10 euroa")

	def test_syo_edullisesti_vahentaa_saldoa_oikein(self):

		self.kortti.syo_edullisesti()

		self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

	def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):

		self.kortti.syo_maukkaasti()

		self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")

	def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):

		self.kortti.syo_maukkaasti()
		self.kortti.syo_maukkaasti()
		self.kortti.syo_edullisesti()

		self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")
		
	def test_kortille_voi_ladata_rahaa(self):
		self.kortti.lataa_rahaa(25)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

	def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
		self.kortti.lataa_rahaa(200)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")
	
	def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
		self.kortti.syo_maukkaasti()
		self.kortti.syo_maukkaasti()
		self.kortti.syo_maukkaasti()

		self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")
		
	def test_negatiivinen_summa_ei_muuta_saldo(self):
		self.kortti.lataa_rahaa(-25)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")
		
	def test_syömään_edullisesti_kun_saldo_2e50snt(self):
		self.kortti = Maksukortti(2.5)
		
		self.kortti.syo_edullisesti()
		
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 0.0 euroa")
		
	def test_syömään_maukkaasti_kun_saldo_4e(self):
		self.kortti = Maksukortti(4)
		
		self.kortti.syo_maukkaasti()
		
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 0 euroa")
		
		
