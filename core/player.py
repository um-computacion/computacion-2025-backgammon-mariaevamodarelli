class Player:
 
    def __init__(self, name, color):
        self.__name__ = name
        self.__color__ = color
        self.__checkers__ = 15

    def get_name(self):
        return self.__name__
