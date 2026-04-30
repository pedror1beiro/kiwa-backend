import unittest
from main import encontrar_maior_padrao

class TestMaiorPadrao(unittest.TestCase):

    def test_exemplos_base(self):
        self.assertEqual(
            encontrar_maior_padrao([1, 3, 2, 1, 1, 3, 3, 4, 1, 3, 2, 1, 2, 1]), 
            [1, 3, 2, 1]
        )
        self.assertEqual(
            encontrar_maior_padrao([6, 2, 6, 8, 22, 0, 9, 5, 8, 22, 0, 9, 8, 1, 2, 4, 5, 6, 7]), 
            [8, 22, 0, 9]
        )
        self.assertEqual(
            encontrar_maior_padrao([1, 2, 1, 2, 1, 3, 1, 1, 2, 5, 1, 7]), 
            [1, 2]
        )
        self.assertEqual(
            encontrar_maior_padrao([0, 20, 3, 5, 0, 20, 0, 0, 0, 20, 3, 5, 0, 20, 0, 0]), 
            [0, 20, 3, 5, 0, 20, 0, 0]
        )
        self.assertEqual(encontrar_maior_padrao([1, 2, 3]), [])
        self.assertEqual(encontrar_maior_padrao([1, 2, 1, 2]), [1, 2])
        self.assertEqual(encontrar_maior_padrao([1, 2, 1, 2, 1, 2, 1]), [1, 2, 1])

    def test_edge_cases(self):
        self.assertEqual(encontrar_maior_padrao([]), [])
        self.assertEqual(encontrar_maior_padrao([1]), [])
        self.assertEqual(encontrar_maior_padrao([7, 7, 7, 7]), [7, 7])

if __name__ == '__main__':
    unittest.main()