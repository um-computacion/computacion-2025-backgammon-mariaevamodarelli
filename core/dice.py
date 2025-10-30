import random


class Dice:
    """Representa los dos dados del juego Backgammon."""

    def __init__(self):
        """Inicializa los dados en (0,0) antes de la primera tirada."""
        self.__last_roll__ = (0, 0)

    def roll(self):
        """
        Realiza una tirada de los dos dados.
        Devuelve una tupla (d1, d2) con valores aleatorios entre 1 y 6.
        """
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        self.__last_roll__ = (d1, d2)
        return self.__last_roll__
    
    def get_last_roll(self):
        """Devuelve la última tirada registrada."""
        return self.__last_roll__

    def is_double(self):
        """Devuelve True si ambos dados tienen el mismo valor."""
        return self.__last_roll__[0] == self.__last_roll__[1]

    def set_last_roll(self, value):
        """
        Establece manualmente el valor de la última tirada.
        Solo se permiten tuplas (0,0) o (d1,d2) con valores entre 1 y 6.
        """
        if (
            isinstance(value, tuple) 
            and len(value) == 2 
            and all(isinstance(v, int) for v in value)
            and (value == (0, 0) or all(1 <= v <= 6 for v in value))
        ):
            self.__last_roll__ = value
        else:
            raise ValueError("last_roll debe ser (0,0) o una tupla (d1,d2) con valores 1..6")
