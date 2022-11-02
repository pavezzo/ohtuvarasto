import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

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

    def test_virheellinen_tilavuus_asettaa_tilavuudeen_nollaan(self):
        self.varasto = Varasto(-1)
        self.assertEqual(self.varasto.tilavuus, 0.0)

    def test_virheellinen_alku_saldo_asettaa_saldon_nollaan(self):
        self.varasto = Varasto(1, -1)
        self.assertEqual(self.varasto.saldo, 0.0)

    def test_saldo_enemman_kuin_tilavuus(self):
        self.varasto = Varasto(10, 100)
        self.assertEqual(self.varasto.saldo, 10)

    def test_varastoon_ei_lisata_jos_maara_negatiivinen(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisattava_maara_suurempi_kuin_varastossa_oleva_tila(self):
        self.varasto.lisaa_varastoon(100)
        self.assertEqual(self.varasto.saldo, 10)

    def test_varastosta_ei_voi_ottaa_negatiivista_maaraa(self):
        otettu = self.varasto.ota_varastosta(-10)
        self.assertEqual(otettu, 0)

    def test_ota_varastosta_maara_enemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(10)
        otettu = self.varasto.ota_varastosta(100)
        self.assertEqual(otettu, 10)

    def test_varasto_on_tekstina_oikein(self):
        self.varasto.lisaa_varastoon(5)
        teksti = str(self.varasto)
        self.assertEqual(teksti, "saldo = 5, vielä tilaa 5")
