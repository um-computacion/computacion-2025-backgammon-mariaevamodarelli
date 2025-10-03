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
    def reset_starting_position(self):

       
        self.__points__ = [0] * 24

        iniciales = {
            0: 2,   
            5: 5,   
            7: 3,   
            11: 5,  
            12: 5,  
            16: 3,  
            18: 5,  
            23: 2   
        }
        for idx, cantidad in iniciales.items():
            self.__points__[idx] = cantidad

    def get_total_checkers(self):
        return sum(self.__points__)

    def clear_board(self):
        self.__points__ = [0] * 24

    def is_empty(self):
        return all(v == 0 for v in self.__points__)

    def get_non_empty_points(self):
        return [i for i, v in enumerate(self.__points__) if v > 0]

    def has_checkers_at(self, index):
        if isinstance(index, int) and 0 <= index < 24:
            return self.__points__[index] > 0
        raise ValueError("El índice debe estar entre 0 y 23")

    def move_checkers(self, from_idx, to_idx, n=1):

        if (isinstance(from_idx, int) and isinstance(to_idx, int) and
            0 <= from_idx < 24 and 0 <= to_idx < 24 and
            isinstance(n, int) and n > 0):
            if self.__points__[from_idx] >= n:
                self.__points__[from_idx] -= n
                self.__points__[to_idx] += n
            else:
                raise ValueError("No hay suficientes fichas en el punto de origen")
        else:
            raise ValueError("Parámetros inválidos para mover fichas")
