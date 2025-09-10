class Player:
 
    def __init__(self, name, color):
        self.__name__ = name
        self.__color__ = color
        self.__checkers__ = 15

    def get_name(self):
        return self.__name__

    def set_name(self, value):
        self.__name__ = value

    def get_color(self):
        return self.__color__

    def set_color(self, value):
        self.__color__ = value

    def get_checkers(self):
        return self.__checkers__

    def set_checkers(self, value):

        if isinstance(value, int) and value >= 0:
            self.__checkers__ = value
        else:
            raise ValueError("La cantidad de fichas debe ser un entero >= 0")
