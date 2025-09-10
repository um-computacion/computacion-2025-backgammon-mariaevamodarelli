import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_initialization(self):
        player = Player("Eva", "blanco")
        self.assertEqual(player.__name__, "Eva")
        self.assertEqual(player.__color__, "blanco")
        self.assertEqual(player.__checkers__, 15)

    def test_get_name_returns_player_name(self):
        player = Player("Juan", "negro")
        self.assertEqual(player.get_name(), "Juan")

    def test_set_name_changes_player_name(self):
        player = Player("Eva", "blanco")
        player.set_name("Ana")
        self.assertEqual(player.__name__, "Ana")

    def test_get_color_returns_player_color(self):
        player = Player("Eva", "blanco")
        self.assertEqual(player.get_color(), "blanco")

    def test_set_color_changes_player_color(self):
        player = Player("Eva", "blanco")
        player.set_color("negro")
        self.assertEqual(player.__color__, "negro")

    def test_get_checkers_starts_at_15(self):
        player = Player("Eva", "blanco")
        self.assertEqual(player.get_checkers(), 15)

    def test_set_checkers_accepts_non_negative_int(self):
        player = Player("Eva", "blanco")
        player.set_checkers(12)
        self.assertEqual(player.__checkers__, 12)
        
if __name__ == "__main__":
    unittest.main()
