import unittest
from Ex03 import find_the_biggest, find_the_smaller

# Testes unitários
class TestComparacaoTresNumeros(unittest.TestCase):
    def test_find_the_biggest(self):
        self.assertEqual(find_the_biggest(10, 5, 8), 10, "Erro: O maior número deveria ser 10.")
        self.assertEqual(find_the_biggest(1, 3, 2), 3, "Erro: O maior número deveria ser 3.")
        self.assertEqual(find_the_biggest(7, 7, 7), 7, "Erro: O maior número deveria ser 7.")
        self.assertEqual(find_the_biggest(-5, -1, -3), -1, "Erro: O maior número deveria ser -1.")

    def test_find_the_smaller(self):
        self.assertEqual(find_the_smaller(10, 5, 8), 5, "Erro: O menor número deveria ser 5.")
        self.assertEqual(find_the_smaller(1, 3, 2), 1, "Erro: O menor número deveria ser 1.")
        self.assertEqual(find_the_smaller(7, 7, 7), 7, "Erro: O menor número deveria ser 7.")
        self.assertEqual(find_the_smaller(-5, -1, -3), -5, "Erro: O menor número deveria ser -5.")

unittest.TextTestRunner().run(unittest.makeSuite(TestComparacaoTresNumeros))
