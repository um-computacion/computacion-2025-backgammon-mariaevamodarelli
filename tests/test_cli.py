import unittest
from core.board import Board
from core.dice import Dice
from core.player import Player
import cli  # tu archivo CLI (test_game.py renombrado o importado)

class TestCLI(unittest.TestCase):


    def test_dados_generan_valores_validos(self):
        """Verifica que los dados del CLI generen valores entre 1 y 6."""
        dice = Dice()
        d1, d2 = dice.roll()
        self.assertTrue(1 <= d1 <= 6)
        self.assertTrue(1 <= d2 <= 6)

    def test_board_reset_crea_24_puntos(self):
        """Verifica que el tablero tenga 24 posiciones después de reset."""
        board = Board()
        board.reset_starting_position()
        self.assertEqual(len(board.get_points()), 24)

    def test_jugadores_tienen_color_correcto(self):
        """Verifica que los jugadores del CLI tengan color asignado."""
        p1 = Player("María", "blanco")
        p2 = Player("Juan", "negro")

        self.assertEqual(p1.get_color(), "blanco")
        self.assertEqual(p2.get_color(), "negro")

    def test_inicializacion_main_componentes(self):
        """Simula la inicialización del CLI sin ejecutar el loop."""
        board = Board()
        dice = Dice()
        p1 = Player("A", "blanco")
        p2 = Player("B", "negro")

        self.assertIsNotNone(board)
        self.assertIsNotNone(dice)
        self.assertEqual(p1.get_color(), "blanco")
        self.assertEqual(p2.get_color(), "negro")

if __name__ == '__main__':
    unittest.main()
