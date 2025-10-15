import unittest
from core.player import Player
from core.board import Board
from core.dice import Dice
from core.game import BackgammonGame

class TestBackgammonGame(unittest.TestCase):

    def test_game_initialization_and_getters(self):
        p1 = Player("Eva", "blanco")
        p2 = Player("Carla", "negro")
        b = Board()
        d = Dice()

        game = BackgammonGame(p1, p2, b, d)

        self.assertIs(game.get_player1(), p1)
        self.assertIs(game.get_player2(), p2)
        self.assertIs(game.get_board(), b)
        self.assertIs(game.get_dice(), d)

    def test_start_game_resets_board_and_rolls_dice(self):
        p1 = Player("Eva", "blanco")
        p2 = Player("Carla", "negro")
        b = Board()
        d = Dice()

        game = BackgammonGame(p1, p2, b, d)
        result = game.start_game()

        self.assertEqual(sum(game.get_board().get_points()), 30)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(1 <= v <= 6 for v in result))

    def test_restart_game_resets_board_and_rolls_dice(self):
        p1 = Player("Eva", "blanco")
        p2 = Player("Carla", "negro")
        b = Board()
        d = Dice()

        game = BackgammonGame(p1, p2, b, d)
        game.start_game()  
        result = game.restart_game()

        self.assertEqual(sum(game.get_board().get_points()), 30)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(1 <= v <= 6 for v in result))


if __name__ == "__main__":
    unittest.main()
