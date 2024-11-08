import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_alku_saldo_miinuksella(self):
        #Väärä alku_saldo
        self.varasto = Varasto(10, -5)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_vaara_tilavuus(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_taynna(self):
        # Yritä lisätä varastoon enemmän kuin on tilaa
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_tyhjavarasto(self):
        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_saldo_loppu(self):
        self.varasto.lisaa_varastoon(8)

        # Yritä ottaa varastosta enemmän tavaraa kuin saldoa on
        saatu_maara = self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(saatu_maara, 8)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_negatiivinen(self):
        saatu_maara = self.varasto.ota_varastosta(-5)

        #Negatiivisen määrän otto
        self.assertAlmostEqual(saatu_maara, 0)

    def test_lisaanegatiivinen(self):
        self.varasto.lisaa_varastoon(-5)

        #Negatiivisen luvun lisäys
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_vastaus(self):
        self.varasto = Varasto(10, 5)

        #Testaa tekstin oikeus
        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")