class Player:
    """Representa un jugador del Backgammon."""

    def __init__(self, name, color):
        """Inicializa un jugador con nombre, color y 15 fichas."""
        self.__name__ = name
        self.__color__ = color
        self.__checkers__ = 15

    def get_name(self):
        """Devuelve el nombre del jugador."""
        return self.__name__
    
    def set_name(self, value):
        """Setea el nombre del jugador, no puede ser vacío."""
        if isinstance(value, str) and value.strip():
            self.__name__ = value
        else:
            raise ValueError("El nombre no puede ser vacío")

    def get_color(self):
        """Devuelve el color del jugador."""
        return self.__color__

    def set_color(self, value):
        """Setea el color del jugador, no puede ser vacío."""
        if isinstance(value, str) and value.strip():
            self.__color__ = value
        else:
            raise ValueError("El color no puede ser vacío")

    def get_checkers(self):
        """Devuelve la cantidad de fichas actuales del jugador."""
        return self.__checkers__

    def set_checkers(self, value):
        """
        Setea la cantidad de fichas del jugador.
        Debe ser un entero entre 0 y 15.
        """
        if isinstance(value, int) and 0 <= value <= 15:
            self.__checkers__ = value
        else:
            raise ValueError("La cantidad de fichas debe ser un entero entre 0 y 15")
