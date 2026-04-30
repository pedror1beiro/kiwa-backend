import unittest
from main import parse_linha, normalizar_timestamp
from datetime import datetime


class TestParseLinha(unittest.TestCase):

    def test_linha_completa(self):
        r = parse_linha("[2026-04-30-08-14, 0.3, 1.2, -0.5, O Pedro entrou]")
        self.assertEqual(r["timestamp"], "2026-04-30-08-14")
        self.assertEqual(r["values"], [0.3, 1.2, -0.5])
        self.assertEqual(r["comment"], "O Pedro entrou")

    def test_so_timestamp(self):
        r = parse_linha("[2026-04-30-06-58]")
        self.assertEqual(r["timestamp"], "2026-04-30-06-58")
        self.assertIsNone(r["values"])
        self.assertIsNone(r["comment"])

    def test_so_timestamp_e_comment(self):
        r = parse_linha("[2026-04-30-09-45, O Carlos saiu do edificio]")
        self.assertIsNone(r["values"])
        self.assertEqual(r["comment"], "O Carlos saiu do edificio")

    def test_so_timestamp_e_values(self):
        r = parse_linha("[2026-04-30-14-50, -0.8, 1.5, 3.3]")
        self.assertEqual(r["values"], [-0.8, 1.5, 3.3])
        self.assertIsNone(r["comment"])

    def test_notacao_cientifica(self):
        # 1e2 e 1e3 devem ser convertidos para float
        r = parse_linha("[2026-04-30-10-05, 1e3, 0.5, O António abriu a porta]")
        self.assertEqual(r["values"], [1000.0, 0.5])

    def test_linha_invalida(self):
        self.assertIsNone(parse_linha("linha sem formato correto"))
        self.assertIsNone(parse_linha(""))

    def test_comment_com_virgula(self):
        # Comentário com vírgula deve ser reconstituído
        r = parse_linha("[2026-04-30-11-30, 1.0, primeiro campo, segundo campo]")
        self.assertEqual(r["comment"], "primeiro campo, segundo campo")


class TestNormalizarTimestamp(unittest.TestCase):

    def test_timestamp_normal(self):
        dt = normalizar_timestamp("2026-04-30-08-14")
        self.assertEqual(dt, datetime(2026, 4, 30, 8, 14))

    def test_timestamp_sem_zeros(self):
        # Mês, dia, hora e minuto sem zero à esquerda
        dt = normalizar_timestamp("2026-4-5-9-3")
        self.assertEqual(dt, datetime(2026, 4, 5, 9, 3))

    def test_ordenacao(self):
        timestamps = ["2026-04-30-20-15", "2026-04-30-06-58", "2026-04-30-12-00"]
        ordenados = sorted(timestamps, key=normalizar_timestamp)
        self.assertEqual(ordenados[0], "2026-04-30-06-58")
        self.assertEqual(ordenados[-1], "2026-04-30-20-15")


if __name__ == '__main__':
    unittest.main()