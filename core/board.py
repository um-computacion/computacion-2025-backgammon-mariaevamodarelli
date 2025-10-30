class Board:
    """Representa el tablero de Backgammon con 24 posiciones."""

    def __init__(self):
        self.__points__ = [{"count": 0, "color": None} for _ in range(24)]
        self.bar_blanco = []  # fichas blancas capturadas
        self.bar_negro = []   # fichas negras capturadas

    # === Getters básicos ===
    def get_points(self):
        return self.__points__

    def get_point(self, index):
        if isinstance(index, int) and 0 <= index < 24:
            return self.__points__[index]
        raise ValueError("El índice debe estar entre 0 y 23")

    # === Direcciones ===
    def distance_in_direction(self, color, from_idx, to_idx):
        """Calcula la distancia de movimiento según el sentido real del tablero."""
        # Blanco mueve de 23 -> 0 (izquierda)
        # Negro mueve de 0 -> 23 (derecha)
        if color == "blanco":
            return from_idx - to_idx
        else:
            return to_idx - from_idx
    

    def can_move(self, from_idx, to_idx):
        if from_idx < 0 or from_idx > 23 or to_idx < 0 or to_idx > 23:
            return False, "Movimiento fuera del tablero"

        origen = self.__points__[from_idx]
        destino = self.__points__[to_idx]

        if origen["count"] == 0:
            return False, "No hay fichas para mover"

        color = origen["color"]

        if self.distance_in_direction(color, from_idx, to_idx) <= 0:
            return False, "Dirección inválida para tu color"

        if destino["count"] == 0 or destino["color"] == color:
            return True, "OK"

        if destino["count"] == 1 and destino["color"] != color:
            return True, "OK (comer)"

        return False, "Movimiento bloqueado"

    # === Inicialización estándar ===
    def reset_starting_position(self):
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

        self.bar_blanco = []
        self.bar_negro = []

    # === Movimiento normal ===
    def move_checker(self, from_idx, to_idx):
        """Mueve una ficha si el movimiento es válido según las reglas básicas del backgammon."""
        if from_idx < 0 or from_idx > 23 or to_idx < 0 or to_idx > 23:
            return "Movimiento fuera del tablero"

        origen = self.__points__[from_idx]
        destino = self.__points__[to_idx]

        if origen["count"] == 0:
            return "No hay fichas para mover"

        color = origen["color"]

        # --- Dirección correcta por color ---
        # Blanco (abajo) → de derecha a izquierda (índices más grandes → más chicos)
        if color == "blanco" and to_idx >= from_idx:
            return "Dirección inválida para blanco"

        # Negro (arriba) → de izquierda a derecha (índices más chicos → más grandes)
        if color == "negro" and to_idx <= from_idx:
            return "Dirección inválida para negro"

        # --- Movimiento válido ---
        # Casilla libre o propia
        if destino["count"] == 0 or destino["color"] == color:
            origen["count"] -= 1
            if origen["count"] == 0:
                origen["color"] = None

            destino["count"] += 1
            destino["color"] = color
            return f"{color} movió de {from_idx} a {to_idx}"

        # --- Comer ficha enemiga ---
        elif destino["count"] == 1 and destino["color"] != color:
            enemigo = destino["color"]
            if enemigo == "blanco":
                self.bar_blanco.append(1)
            else:
                self.bar_negro.append(1)

            destino["color"] = color
            destino["count"] = 1

            origen["count"] -= 1
            if origen["count"] == 0:
                origen["color"] = None

            return f"{color} comió una ficha de {enemigo} en {to_idx} (enviada al bar)"
        else:
            return "Movimiento bloqueado"

    # === Control del bar ===
    def has_bar(self, color):
        if color == "blanco":
            return len(self.bar_blanco) > 0
        else:
            return len(self.bar_negro) > 0

    def reenter_from_bar(self, color, dice_values):
        """Intenta reintroducir una ficha desde el bar usando los valores de los dados."""
        # determinar rango del tablero del oponente
        if color == "blanco":
            # entra en la zona del rival: puntos 0-5
            base = 0
            bar_list = self.bar_blanco
        else:
            # entra en 18-23
            base = 18
            bar_list = self.bar_negro

        posibles = []
        for d in dice_values:
            destino = base + (d - 1)
            punto = self.__points__[destino]
            if punto["count"] == 0 or (punto["count"] == 1 and punto["color"] != color):
                posibles.append(destino)

        if not posibles:
            return False, "No hay espacios disponibles para reingresar."

        # usar el primer dado disponible
        destino = posibles[0]
        punto = self.__points__[destino]
        if punto["count"] == 1 and punto["color"] != color:
            # come la ficha rival
            if color == "blanco":
                self.bar_negro.append(1)
            else:
                self.bar_blanco.append(1)
        punto["count"] += 1
        punto["color"] = color
        bar_list.pop()  # sacar ficha del bar

        return True, f"{color} reingresó ficha en punto {destino}"
