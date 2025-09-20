import random


class Dice:
    def __init__(self):
        self.__last_roll__ = (0, 0)

    def roll(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        self.__last_roll__ = (d1, d2)
        return self.__last_roll__
    
    def get_last_roll(self):
        return self.__last_roll__

    def is_double(self):

        return self.__last_roll__[0] == self.__last_roll__[1]

    def set_last_roll(self, value):
        if (
            isinstance(value, tuple) 
            and len(value) == 2 
            and all(isinstance(v, int) for v in value)
            and (value == (0, 0) or all(1 <= v <= 6 for v in value))
        ):
            self.__last_roll__ = value
        else:
            raise ValueError("last_roll debe ser (0,0) o una tupla (d1,d2) con valores 1..6")

