import unittest

from par import es_par

class Tests(unittest.TestCase):
    def test_1(self):
        """Esto revisa si 1 no es par"""
        self.assertFalse(es_par(1))

    def test_3(self):
        """Esto revisa si 3 no es par"""
        self.assertFalse(es_par(3))

    def test_4(self):
        """Esto revisa si 4 es par"""
        self.assertTrue(es_par(4))

    def test_8(self):
        """Esto revisa si 8 es par"""
        self.assertTrue(es_par(8))

if __name__ == "__main__":
    unittest.main()