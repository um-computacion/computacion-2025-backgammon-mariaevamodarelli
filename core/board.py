class Board:
    """Representa el tablero de Backgammon con 24 posiciones."""

    def __init__(self):
        self.__points__ = [{"count": 0, "color": None} for _ in range(24)]
        self.captured_blanco = []
        self.captured_negro = []



    def get_points(self):
        """Devuelve la lista completa de puntos del tablero."""
        return self.__points__

    def get_point(self, index):
        """Devuelve el diccionario {'count': n, 'color': c} en un punto específico."""
        if isinstance(index, int) and 0 <= index < 24:
            return self.__points__[index]
        raise ValueError("El índice debe estar entre 0 y 23")

    def set_point(self, index, count, color):
        """Asigna una cantidad y color de fichas a un punto determinado."""
        if (isinstance(index, int) and 0 <= index < 24
                and isinstance(count, int) and count >= 0):
            self.__points__[index]["count"] = count
            self.__points__[index]["color"] = color
        else:
            raise ValueError("index 0..23 y count entero >= 0")

    def reset_starting_position(self):
        """Reinicia el tablero con la posición inicial estándar de Backgammon."""
        self.__points__ = [{"count": 0, "color": None} for _ in range(24)]

        setup = [
            (0, 2, "blanco"),
            (5, 5, "negro"),
            (7, 3, "negro"),
            (11, 5, "blanco"),
            (12, 5, "negro"),
            (16, 3, "blanco"),
            (18, 5, "blanco"),
            (23, 2, "negro"),
        ]

        for pos, cantidad, color in setup:
            self.__points__[pos]["count"] = cantidad
            self.__points__[pos]["color"] = color

    def get_total_checkers(self):
        """Devuelve el total de fichas en el tablero."""
        return sum(p["count"] for p in self.__points__)

    def clear_board(self):
        """Vacía todas las posiciones del tablero."""
        self.__points__ = [{"count": 0, "color": None} for _ in range(24)]

    def is_empty(self):
        """Devuelve True si todas las posiciones están vacías."""
        return all(p["count"] == 0 for p in self.__points__)

    def get_non_empty_points(self):
        """Devuelve los índices de los puntos que contienen fichas."""
        return [i for i, p in enumerate(self.__points__) if p["count"] > 0]

    def reset_board(self):
        """Reinicia el tablero a 24 posiciones vacías."""
        self.__points__ = [{"count": 0, "color": None} for _ in range(24)]

    # === MOVIMIENTO DE FICHAS ===

    def move_checker(self, from_idx, to_idx):
        """Mueve una ficha si el movimiento es válido según las reglas básicas del backgammon."""
        if from_idx < 0 or from_idx > 23 or to_idx < 0 or to_idx > 23:
            return "Movimiento fuera del tablero"

        origen = self.__points__[from_idx]
        destino = self.__points__[to_idx]

        if origen["count"] == 0:
            return "No hay fichas para mover"

        color = origen["color"]

        # Dirección del movimiento según el color
        if color == "blanco" and to_idx <= from_idx:
            return "Dirección inválida para blanco"
        if color == "negro" and to_idx >= from_idx:
            return "Dirección inválida para negro"

        # Casilla libre o propia → movimiento válido
        if destino["count"] == 0 or destino["color"] == color:
            origen["count"] -= 1
            if origen["count"] == 0:
                origen["color"] = None

            destino["count"] += 1
            destino["color"] = color
            return f"{color} movió de {from_idx} a {to_idx}"

        # Comer ficha enemiga (solo si hay 1)
        elif destino["count"] == 1 and destino["color"] != color:
            enemigo = destino["color"]
            if enemigo == "blanco":
                self.captured_blanco.append(to_idx)
            else:
                self.captured_negro.append(to_idx)

            destino["color"] = color
            destino["count"] = 1

            origen["count"] -= 1
            if origen["count"] == 0:
                origen["color"] = None

            return f"{color} comió una ficha de {enemigo} en {to_idx}"

        else:
            return "Movimiento bloqueado"

    def can_move(self, from_idx, to_idx):
        """Valida reglas básicas: tablero, hay ficha, dirección, bloqueos/comer."""
        if from_idx < 0 or from_idx > 23 or to_idx < 0 or to_idx > 23:
            return False, "Movimiento fuera del tablero"

        origen = self.__points__[from_idx]
        destino = self.__points__[to_idx]

        if origen["count"] == 0:
            return False, "No hay fichas para mover"

        color = origen["color"]

        # Dirección
        if color == "blanco" and to_idx <= from_idx:
            return False, "Dirección inválida para blanco"
        if color == "negro" and to_idx >= from_idx:
            return False, "Dirección inválida para negro"

        # Destino: vacío o propio → ok
        if destino["count"] == 0 or destino["color"] == color:
            return True, "OK"

        # Blot: exactamente 1 del rival → se puede
        if destino["count"] == 1 and destino["color"] != color:
            return True, "OK (comer)"

        # Bloqueado
        return False, "Movimiento bloqueado"

    def distance_in_direction(self, color, from_idx, to_idx):
        """Devuelve la distancia positiva en el sentido correcto para ese color; si es negativa/0, no es válida."""
        if color == "blanco":
            return to_idx - from_idx  # debe ser > 0
        else:
            return from_idx - to_idx  # debe ser > 0
