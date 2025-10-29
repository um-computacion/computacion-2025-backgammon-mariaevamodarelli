import pygame
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.board import Board
from core.dice import Dice
from core.player import Player
from core.game import BackgammonGame


def pedir_nombres():
    """Pide los nombres en la terminal antes de iniciar el juego."""
    n1 = input("Nombre del jugador 1 (blanco): ").strip() or "Jugador 1"
    n2 = input("Nombre del jugador 2 (negro): ").strip() or "Jugador 2"
    return n1, n2


class BackgammonUI:
    def __init__(self, name1, name2, screen):
        self.screen = screen
        self.board = Board()
        self.dice = Dice()
        self.player1 = Player(name1, "blanco")
        self.player2 = Player(name2, "negro")
        self.turn = self.player1
        self.game = BackgammonGame(self.player1, self.player2, self.board, self.dice)
        self.board.reset_starting_position()
        self.last_roll = (0, 0)
        self.selected_point = None
        self.message = "Presioná ESPACIO para tirar los dados"
        self.awaiting_move = False
        self.remaining_dice = []   # lista de dados pendientes del turno actual


        # Colores y fuentes
        self.WOOD = (205, 170, 125)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (220, 20, 60)
        self.BLUE = (30, 144, 255)
        self.GREY = (200, 200, 200)
        self.DARK = (40, 40, 40)
        self.FONT = pygame.font.SysFont("arial", 22)

    def draw_board(self):
        self.screen.fill(self.WOOD)
        triangle_width = 50
        triangle_height = 250

        for i in range(12):
            color = self.RED if i % 2 == 0 else self.GREY
            points = [
                (i * triangle_width, 0),
                ((i + 1) * triangle_width, 0),
                (i * triangle_width + triangle_width / 2, triangle_height)
            ]
            pygame.draw.polygon(self.screen, color, points)

        for i in range(12):
            color = self.BLUE if i % 2 == 0 else self.GREY
            points = [
                (i * triangle_width, 650),
                ((i + 1) * triangle_width, 650),
                (i * triangle_width + triangle_width / 2, 650 - triangle_height)
            ]
            pygame.draw.polygon(self.screen, color, points)

        points = self.board.get_points()
        for i, p in enumerate(points):
            if p["count"] > 0:
                color = self.WHITE if p["color"] == "blanco" else self.BLACK
                for j in range(p["count"]):
                    if i < 12:
                        x = i * triangle_width + triangle_width / 2
                        y = triangle_height - (j * 25) - 20
                    else:
                        x = (i - 12) * triangle_width + triangle_width / 2
                        y = 650 - triangle_height + (j * 25) + 20
                    pygame.draw.circle(self.screen, color, (int(x), int(y)), 12)
                    if self.selected_point == i:
                        pygame.draw.circle(self.screen, (255, 215, 0), (int(x), int(y)), 14, 2)

    def draw_panel(self):
        panel = pygame.Rect(800, 100, 280, 250)
        pygame.draw.rect(self.screen, (245, 245, 245), panel, border_radius=10)
        pygame.draw.rect(self.screen, self.DARK, panel, 2, border_radius=10)

        turno_text = self.FONT.render(f"Turno: {self.turn.get_name()} ({self.turn.get_color()})", True, self.DARK)
        self.screen.blit(turno_text, (820, 120))

        d1, d2 = self.last_roll
        self.screen.blit(self.FONT.render(f"Dado 1: {d1}", True, self.DARK), (820, 160))
        self.screen.blit(self.FONT.render(f"Dado 2: {d2}", True, self.DARK), (820, 190))
        self.screen.blit(self.FONT.render(self.message, True, self.DARK), (810, 230))

    def get_clicked_point(self, pos):
        x, y = pos
        triangle_width = 50
        if x > 600:
            return None
        col = int(x // triangle_width)
        return col if y < 325 else 12 + col

    def roll_dice(self):
        self.last_roll = self.dice.roll()
        d1, d2 = self.last_roll
        # preparar dados restantes
        if d1 == d2:
            self.remaining_dice = [d1, d1, d1, d1]  # dobles = 4 movimientos
        else:
            self.remaining_dice = [d1, d2]
        self.message = f"Tiraste {d1} y {d2}. Elegí ficha para mover."
        self.awaiting_move = True
        self.selected_point = None

    def handle_click(self, pos):
        point = self.get_clicked_point(pos)
        if point is None:
            return

        if self.selected_point is None:
            # Seleccionar origen
            p = self.board.get_point(point)
            if p["color"] == self.turn.get_color() and p["count"] > 0:
                self.selected_point = point
                self.message = f"Origen {point} seleccionado. Elegí destino (dados: {self.remaining_dice})."
            else:
                self.message = "No podés mover esa ficha."
            return

        # Ya teníamos origen → ahora destino
        origen = self.selected_point
        destino = point
        color = self.turn.get_color()

        # 1) distancia según color (debe ser > 0)
        dist = self.board.distance_in_direction(color, origen, destino)
        if dist <= 0:
            self.message = "Destino en sentido inválido para tu color."
            return

        # 2) ¿existe un dado con esa distancia?
        if dist not in self.remaining_dice:
            self.message = f"Ese destino no coincide con tus dados {self.remaining_dice}."
            return

        # 3) ¿pasa reglas básicas del tablero?
        ok, why = self.board.can_move(origen, destino)
        if not ok:
            self.message = why
            return

        # 4) ejecutar movimiento real
        result = self.board.move_checker(origen, destino)
        self.message = result

        # 5) consumir un dado con esa distancia (una sola vez)
        self.remaining_dice.remove(dist)

        # 6) limpiar selección
        self.selected_point = None

        # 7) si no quedan dados → cerrar turno
        if not self.remaining_dice:
            self.awaiting_move = False
            self.turn = self.player2 if self.turn == self.player1 else self.player1
            self.message += " | Turno del siguiente jugador."
        else:
            self.message += f" | Mové de nuevo (dados: {self.remaining_dice})."



    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if not self.awaiting_move:
                        self.roll_dice()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.awaiting_move:
                    self.handle_click(event.pos)

            self.draw_board()
            self.draw_panel()
            pygame.display.flip()
            clock.tick(30)


if __name__ == "__main__":
    # Primero pedimos los nombres
    n1, n2 = pedir_nombres()

    # Ahora iniciamos PyGame
    pygame.init()
    screen = pygame.display.set_mode((1100, 650))
    pygame.display.set_caption("Backgammon - Computación 2025")

    ui = BackgammonUI(n1, n2, screen)
    ui.run()
