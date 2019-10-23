import unittest
from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        
        """Check that 1 is not prime."""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """Check that 2 is prime."""
        self.assertTrue(is_prime(2))

    def test_8(self):
        """Check that 8 is not prime."""
        self.assertFalse(is_prime(8))

    def test_25(self):
        """Check that 25 is not prime."""
        self.assertFalse(is_prime(25))
    
    def test_7(self):
        """Check that 7 is prime."""
        self.assertTrue(is_prime(7))

    def test_33(self):
        """Check that 33 is not prime."""
        self.assertFalse(is_prime(33))

if __name__ == "__main__":
    unittest.main()