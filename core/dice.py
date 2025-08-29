import random


class Dice:
    def __init__(self):
        self.__last_roll__ = (0, 0)

    def roll(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        self.__last_roll__ = (d1, d2)
        return self.__last_roll__
