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

if __name__ == "__main__":
    unittest.main()
