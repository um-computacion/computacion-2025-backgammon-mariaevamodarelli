import unittest
from core.board import Board

class TestBoard(unittest.TestCase):

    def test_board_initializes_with_24_points(self):
        b = Board()
        self.assertEqual(len(b.get_points()), 24)
        self.assertTrue(all(v == 0 for v in b.get_points()))

    def test_get_point_valid_indices(self):
        b = Board()
        self.assertEqual(b.get_point(0), 0)
        self.assertEqual(b.get_point(23), 0)

    def test_set_point_updates_value(self):
        b = Board()
        b.set_point(5, 3)
        self.assertEqual(b.get_point(5), 3)

    def test_get_point_invalid_index_throws(self):
        b = Board()
        try:
            b.get_point(24)
            self.fail("No lanzó ValueError con índice fuera de rango (24)")
        except ValueError:
            pass
        try:
            b.get_point(-1)
            self.fail("No lanzó ValueError con índice negativo (-1)")
        except ValueError:
            pass

    def test_set_point_invalid_index_throws(self):
        b = Board()
        try:
            b.set_point(24, 1)
            self.fail("No lanzó ValueError con índice fuera de rango (24)")
        except ValueError:
            pass
        try:
            b.set_point(-1, 1)
            self.fail("No lanzó ValueError con índice negativo (-1)")
        except ValueError:
            pass

    def test_set_point_negative_value_throws(self):
        b = Board()
        try:
            b.set_point(0, -1)
            self.fail("No lanzó ValueError con valor negativo (-1)")
        except ValueError:
            pass

    def test_set_point_wrong_types_throw(self):
        b = Board()
        try:
            b.set_point("0", 1)
            self.fail("No lanzó ValueError con índice no entero ('0')")
        except ValueError:
            pass
        try:
            b.set_point(0, "uno")
            self.fail("No lanzó ValueError con valor no entero ('uno')")
        except ValueError:
            pass

if __name__ == "__main__":
    unittest.main()

