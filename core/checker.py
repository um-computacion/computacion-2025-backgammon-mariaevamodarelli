class Checker:
    """
    Representa una ficha de Backgammon.
    Mantengo el diseño simple a propósito: solo color.
    No uso tipado fuerte.
    """
    def __init__(self, color):
        # color: "blanco" o "negro"
        if not isinstance(color, str) or color.strip() == "":
            raise ValueError("El color de la ficha no puede ser vacío")
        if color not in ("blanco", "negro"):
            raise ValueError("Color inválido para Checker")
        self.__color__ = color

    def get_color(self):
        """Devuelve el color de la ficha."""
        return self.__color__
