class Board:
    """Representa el tablero de Backgammon con 24 posiciones."""

    def __init__(self):
        """Inicializa un tablero vacío con 24 puntos."""
        self.__points__ = [{"count": 0, "color": None} for _ in range(24)]

    def get_points(self):
        """Devuelve la lista completa de puntos del tablero."""
        return self.__points__
    
    def get_point(self, index):
        """Devuelve el diccionario {'count': n, 'color': c} en un punto específico."""
        if isinstance(index, int) and 0 <= index < 24:
            return self.__points__[index]
        raise ValueError("El índice debe estar entre 0 y 23")

    def set_point(self, index, count, color):
        """
        Asigna una cantidad y color de fichas a un punto determinado.
        Valida que el índice sea 0..23, el valor entero >= 0 y el color válido.
        """
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

    def move_checker(self, from_index, to_index):
        """
        Mueve una ficha desde un punto a otro del tablero.

        Reglas básicas:
        - El índice de origen y destino debe ser válido (0..23).
        - Debe haber al menos una ficha en el origen.
        - Si el destino tiene color contrario con más de 1 ficha, el movimiento es inválido.
        - Si el destino tiene solo 1 ficha del oponente, la "come" (la reemplaza).
        - En caso válido, se resta 1 del origen y se suma 1 al destino.
        """
        if not (0 <= from_index < 24 and 0 <= to_index < 24):
            raise ValueError("Los índices deben estar entre 0 y 23")

        origen = self.__points__[from_index]
        destino = self.__points__[to_index]

        if origen["count"] == 0:
            return "No hay fichas en el punto de origen"

        if destino["color"] is None or destino["color"] == origen["color"]:
            origen["count"] -= 1
            if origen["count"] == 0:
                origen["color"] = None
            destino["count"] += 1
            destino["color"] = origen["color"]
            return "Movimiento válido"

        if destino["count"] == 1 and destino["color"] != origen["color"]:
            # comer ficha
            destino["color"] = origen["color"]
            return "Ficha comida y movimiento válido"

        return "Movimiento inválido: punto bloqueado"
