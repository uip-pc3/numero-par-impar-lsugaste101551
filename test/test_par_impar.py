import unittest
from app.main import par_impar

class Testpar(unittest.TestCase):
    def test_par_impar(self):
        self.assertEqual(par_impar(4), "Par")
        self.assertEqual(par_impar(5), "Inpar")

if __name__ == '__main__':
    unittest.main()