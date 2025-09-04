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

if __name__ == "__main__":
    unittest.main()
