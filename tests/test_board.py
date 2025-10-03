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


    def test_reset_starting_position_sets_expected_counts(self):
        b = Board()
        b.reset_starting_position()
        self.assertEqual(len(b.get_points()), 24)

        self.assertEqual(b.get_point(0), 2)   
        self.assertEqual(b.get_point(5), 5)   
        self.assertEqual(b.get_point(7), 3)   
        self.assertEqual(b.get_point(11), 5)  
        self.assertEqual(b.get_point(12), 5)  
        self.assertEqual(b.get_point(16), 3)  
        self.assertEqual(b.get_point(18), 5)  
        self.assertEqual(b.get_point(23), 2)  

       
        for i, v in enumerate(b.get_points()):
            if i not in (0, 5, 7, 11, 12, 16, 18, 23):
                self.assertEqual(v, 0, f"El punto {i} debería ser 0")

    def test_total_checkers_is_30(self):
        b = Board()
        b.reset_starting_position()
        self.assertEqual(sum(b.get_points()), 30)

    def test_get_total_checkers(self):
        b = Board()
        b.reset_starting_position()
        self.assertEqual(b.get_total_checkers(), 30)  

    def test_clear_board_sets_all_points_to_zero(self):
        b = Board()
        b.set_point(5, 3)
        b.clear_board()
        self.assertTrue(all(v == 0 for v in b.get_points()))

    def test_is_empty_returns_true_when_board_has_no_checkers(self):
        b = Board()
        b.clear_board()
        self.assertTrue(b.is_empty())

    def test_is_empty_returns_false_when_board_has_checkers(self):
        b = Board()
        b.set_point(0, 1)
        self.assertFalse(b.is_empty())

    def test_get_non_empty_points_returns_correct_indices(self):
        b = Board()
        b.clear_board()
        b.set_point(3, 2)
        b.set_point(7, 5)
        self.assertEqual(b.get_non_empty_points(), [3, 7])

    def test_has_checkers_at_returns_true_if_point_has_checkers(self):
        b = Board()
        b.set_point(5, 2)
        self.assertTrue(b.has_checkers_at(5))

    def test_has_checkers_at_returns_false_if_point_is_empty(self):
        b = Board()
        self.assertFalse(b.has_checkers_at(10))

    def test_move_checkers_moves_one_checker(self):
        b = Board()
        b.set_point(0, 2)
        b.move_checkers(0, 5, 1)
        self.assertEqual(b.get_point(0), 1)
        self.assertEqual(b.get_point(5), 1)


if __name__ == "__main__":
    unittest.main()

