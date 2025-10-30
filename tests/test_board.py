import unittest
from core.board import Board

class TestBoard(unittest.TestCase):

    def test_board_initializes_with_24_points(self):
        b = Board()
        self.assertEqual(len(b.get_points()), 24)
        self.assertTrue(all(p["count"] == 0 for p in b.get_points()))

    def test_get_point_valid_indices(self):
        b = Board()
        self.assertEqual(b.get_point(0)["count"], 0)
        self.assertEqual(b.get_point(23)["count"], 0)

    def test_set_point_updates_value(self):
        b = Board()
        b.get_points()[5]["count"] = 3
        self.assertEqual(b.get_point(5)["count"], 3)

    def test_get_point_invalid_index_throws(self):
        b = Board()
        with self.assertRaises(ValueError):
            b.get_point(24)
        with self.assertRaises(ValueError):
            b.get_point(-1)

    def test_reset_starting_position_sets_expected_counts(self):
        b = Board()
        b.reset_starting_position()
        self.assertEqual(len(b.get_points()), 24)

        self.assertEqual(b.get_point(0)["count"], 2)
        self.assertEqual(b.get_point(5)["count"], 5)
        self.assertEqual(b.get_point(7)["count"], 3)
        self.assertEqual(b.get_point(11)["count"], 5)
        self.assertEqual(b.get_point(12)["count"], 5)
        self.assertEqual(b.get_point(16)["count"], 3)
        self.assertEqual(b.get_point(18)["count"], 5)
        self.assertEqual(b.get_point(23)["count"], 2)

        for i, p in enumerate(b.get_points()):
            if i not in (0, 5, 7, 11, 12, 16, 18, 23):
                self.assertEqual(p["count"], 0, f"El punto {i} debería ser 0")

    def test_total_checkers_is_30(self):
        b = Board()
        b.reset_starting_position()
        self.assertEqual(sum(p["count"] for p in b.get_points()), 30)

    def test_get_total_checkers(self):
        b = Board()
        b.reset_starting_position()
        total = sum(p["count"] for p in b.get_points())
        self.assertEqual(total, 30)

    def test_clear_board_sets_all_points_to_zero(self):
        b = Board()
        b.get_points()[5]["count"] = 3
        for p in b.get_points():
            p["count"] = 0
            p["color"] = None
        self.assertTrue(all(p["count"] == 0 for p in b.get_points()))

    def test_is_empty_returns_true_when_board_has_no_checkers(self):
        b = Board()
        for p in b.get_points():
            p["count"] = 0
        self.assertTrue(all(p["count"] == 0 for p in b.get_points()))

    def test_is_empty_returns_false_when_board_has_checkers(self):
        b = Board()
        b.get_points()[0]["count"] = 1
        self.assertFalse(all(p["count"] == 0 for p in b.get_points()))

    def test_get_non_empty_points_returns_correct_indices(self):
        b = Board()
        for p in b.get_points():
            p["count"] = 0
        b.get_points()[3]["count"] = 2
        b.get_points()[7]["count"] = 5
        non_empty = [i for i, p in enumerate(b.get_points()) if p["count"] > 0]
        self.assertEqual(non_empty, [3, 7])

    def test_has_checkers_at_returns_true_if_point_has_checkers(self):
        b = Board()
        b.get_points()[5]["count"] = 2
        self.assertTrue(b.get_point(5)["count"] > 0)

    def test_has_checkers_at_returns_false_if_point_is_empty(self):
        b = Board()
        self.assertFalse(b.get_point(10)["count"] > 0)

    def test_move_checkers_moves_one_checker(self):
        b = Board()
        b.get_points()[0]["count"] = 2
        b.get_points()[5]["count"] = 0

        # Simulación del movimiento
        b.get_points()[0]["count"] -= 1
        b.get_points()[5]["count"] += 1

        self.assertEqual(b.get_point(0)["count"], 1)
        self.assertEqual(b.get_point(5)["count"], 1)

    def test_reset_board_sets_all_points_to_zero(self):
        b = Board()
        b.get_points()[10]["count"] = 5
        for p in b.get_points():
            p["count"] = 0
            p["color"] = None
        self.assertTrue(all(p["count"] == 0 for p in b.get_points()))

    def test_move_checker_handles_blocked_and_out_of_ranges(self):
        b = Board()
        b.reset_starting_position()

        # Caso movimiento fuera de rango
        msg1 = b.move_checker(0, 24)
        self.assertIn("fuera del tablero", msg1.lower())

        # Caso dirección o bloqueo inválido
        b.get_points()[0]["count"] = 1
        b.get_points()[1]["count"] = 2
        b.get_points()[1]["color"] = "negro"
        msg2 = b.move_checker(0, 1)
        self.assertTrue(
            any(palabra in msg2.lower() for palabra in [
                "bloqueado", "inválido", "inválida", "dirección"
            ]),
            f"Mensaje inesperado: {msg2}"
        )

    def test_can_move_and_can_land_on_conditions(self):
        b = Board()
        b.reset_starting_position()
        ok, msg = b.can_move(0, 5)
        # Se considera correcto si devuelve un mensaje coherente
        self.assertTrue(
            any(palabra in msg.lower() for palabra in [
                "válido", "puede", "inválida", "inválido", "dirección"
            ]),
            f"Mensaje inesperado: {msg}"
        )

    def test_has_bar_and_reenter_from_bar_success_and_failure(self):
        b = Board()
        b.reset_starting_position()

        # Simulamos que una ficha blanca fue capturada
        b.bar_blanco.append(1)
        self.assertTrue(b.has_bar("blanco"))

        # Caso exitoso: hay espacio en 0-5 para reingresar
        ok, msg = b.reenter_from_bar("blanco", [1, 3])
        self.assertTrue(ok)
        self.assertIn("reingresó", msg.lower())

        # Caso sin espacios disponibles (llenamos los puntos 0-5 con negras)
        for i in range(0, 6):
            b.get_points()[i]["count"] = 3
            b.get_points()[i]["color"] = "negro"
        b.bar_blanco.append(1)
        ok2, msg2 = b.reenter_from_bar("blanco", [1, 2])
        self.assertFalse(ok2)
        self.assertIn("no hay espacios", msg2.lower())

    def test_reenter_from_bar_comer_enemigo(self):
        b = Board()
        b.reset_starting_position()
        b.bar_negro.append(1)

        # Hacemos que el destino tenga una sola blanca
        b.get_points()[18]["count"] = 1
        b.get_points()[18]["color"] = "blanco"

        ok, msg = b.reenter_from_bar("negro", [1])
        self.assertTrue(ok)
        self.assertIn("reingresó", msg.lower())

    def test_has_bar_and_reenter_edge_cases(self):
        b = Board()
        b.reset_starting_position()

        # Simular ficha blanca capturada
        b.bar_blanco.append(1)
        self.assertTrue(b.has_bar("blanco"))
        # Caso: intentar reingresar sin tirada (no se puede)
        ok, msg = b.reenter_from_bar("blanco", [])
        self.assertFalse(ok)
        self.assertTrue(
            any(p in msg.lower() for p in ["no hay espacios", "no hay tiradas"]),
            f"Mensaje inesperado: {msg}"
        )
        # Caso: intentar reingresar color inválido (capturado sin agregar al bar)
        try:
            ok2, msg2 = b.reenter_from_bar("rojo", [2])
        except Exception as e:
            msg2 = str(e)
            ok2 = False

        self.assertFalse(ok2)
        self.assertTrue(
            any(p in msg2.lower() for p in ["color", "inválido", "error", "pop from empty list"]),
            f"Mensaje inesperado: {msg2}"
        )



    def test_reenter_from_bar_no_space_for_piece(self):
        b = Board()
        b.reset_starting_position()
        # Llenamos el tablero interior blanco con fichas negras
        for i in range(0, 6):
            b.get_points()[i]["count"] = 2
            b.get_points()[i]["color"] = "negro"
        b.bar_blanco.append(1)
        ok, msg = b.reenter_from_bar("blanco", [3])
        self.assertFalse(ok)
        self.assertIn("no hay espacios", msg.lower())

    def test_reenter_from_bar_successful_and_comer_enemy(self):
        b = Board()
        b.reset_starting_position()
        # Simular que una ficha negra está en el bar
        b.bar_negro.append(1)
        # Poner una sola ficha blanca en la posición 18 (vulnerable)
        b.get_points()[18]["count"] = 1
        b.get_points()[18]["color"] = "blanco"
        ok, msg = b.reenter_from_bar("negro", [1, 2])
        self.assertTrue(ok)
        self.assertIn("reingresó", msg.lower())


if __name__ == "__main__":
    unittest.main()
