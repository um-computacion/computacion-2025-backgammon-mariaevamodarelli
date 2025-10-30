import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):

    def test_checker_color_ok(self):
        c = Checker("blanco")
        self.assertEqual(c.get_color(), "blanco")

    def test_checker_color_invalido(self):
        with self.assertRaises(ValueError):
            Checker("")
        with self.assertRaises(ValueError):
            Checker("rojo")

if __name__ == "__main__":
    unittest.main()
