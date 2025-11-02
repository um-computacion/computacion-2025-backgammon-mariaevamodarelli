class BackgammonGame:
    """Orquesta los componentes principales del juego: jugadores, tablero y dados."""

    def __init__(self, player1, player2, board, dice):
        """Inicializa la partida con los jugadores, el tablero y los dados."""
        self.__player1__ = player1
        self.__player2__ = player2
        self.__board__ = board
        self.__dice__ = dice
        self.__game_over__ = False

    def get_player1(self):
        """Devuelve el jugador 1."""
        return self.__player1__

    def get_player2(self):
        """Devuelve el jugador 2."""
        return self.__player2__

    def get_board(self):
        """Devuelve el tablero del juego."""
        return self.__board__

    def get_dice(self):
        """Devuelve los dados del juego."""
        return self.__dice__

    def start_game(self):
        """
        Inicia la partida:
        - Coloca las fichas en la posición inicial.
        - Realiza la primera tirada de dados.
        """
        self.__board__.reset_starting_position()
        self.__dice__.roll()
        return self.__dice__.get_last_roll()

    def restart_game(self):
        """
        Reinicia la partida:
        - Limpia el tablero.
        - Coloca las fichas nuevamente en la posición inicial.
        - Realiza una nueva tirada de dados.
        """
        self.__board__.reset_board()
        self.__board__.reset_starting_position()
        self.__dice__.roll()
        return self.__dice__.get_last_roll()

    def end_game(self):
        """
        Finaliza la partida:
        - Marca el juego como terminado.
        - Limpia la última tirada de dados.
        """
        self.__game_over__ = True
        self.__dice__.set_last_roll((0, 0))
        return "Juego finalizado"

    def move_checker(self, player, from_point, to_point):
        """
        Mueve una ficha del jugador de from_point a to_point si la jugada es válida.

        Reglas:
        - Solo se pueden mover fichas del color del jugador.
        - El punto destino no puede tener más de una ficha del oponente.
        - Si tiene exactamente una ficha del oponente, la "come".
        """
        points = self.__board__.get_points()

        origen = points[from_point]
        destino = points[to_point]

        # Validar que haya fichas propias
        if origen["color"] != player.get_color() or origen["count"] == 0:
            return "Movimiento inválido: no hay fichas propias."

        # Validar destino
        if destino["color"] == player.get_color() or destino["count"] == 0:
            # Movimiento simple
            origen["count"] -= 1
            if origen["count"] == 0:
                origen["color"] = None
            destino["count"] += 1
            destino["color"] = player.get_color()
            return "Movimiento válido."
        
        if destino["count"] == 1 and destino["color"] != player.get_color():
            # Comer ficha del rival
            destino["color"] = player.get_color()
            return "Ficha comida y movimiento válido."

        return "Movimiento inválido: punto bloqueado."
