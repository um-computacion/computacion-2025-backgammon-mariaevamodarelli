class Board:

    def __init__(self):
        self.__points__ = [0] * 24

    def get_points(self):
        return self.__points__
    
    def get_point(self, index):
            
            if isinstance(index, int) and 0 <= index < 24:
                return self.__points__[index]
            raise ValueError("El índice debe estar entre 0 y 23")

    def set_point(self, index, value):

        if (isinstance(index, int) and 0 <= index < 24
                and isinstance(value, int) and value >= 0):
            self.__points__[index] = value
        else:
            raise ValueError("index 0..23 y value entero >= 0")