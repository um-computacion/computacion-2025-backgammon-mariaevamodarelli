import pygame
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.board import Board
from core.dice import Dice
from core.player import Player
from core.game import BackgammonGame


def pedir_nombres():
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
        self.remaining_dice = []
        self.awaiting_move = False
        self.selected_point = None
        self.message = "Presioná ESPACIO para tirar los dados"

        self.WOOD = (205, 170, 125)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (220, 20, 60)
        self.BLUE = (30, 144, 255)
        self.GREY = (200, 200, 200)
        self.DARK = (40, 40, 40)
        self.FONT = pygame.font.SysFont("arial", 22)

    # === Tablero ===
    def draw_board(self):
        self.screen.fill(self.WOOD)
        triangle_width = 50
        triangle_height = 250

        # fila superior (rojo)
        for i in range(12):
            color = self.RED if i % 2 == 0 else self.GREY
            pts = [
                (i * triangle_width, 0),
                ((i + 1) * triangle_width, 0),
                (i * triangle_width + triangle_width / 2, triangle_height)
            ]
            pygame.draw.polygon(self.screen, color, pts)

        # fila inferior (azul)
        for i in range(12):
            color = self.BLUE if i % 2 == 0 else self.GREY
            pts = [
                (i * triangle_width, 650),
                ((i + 1) * triangle_width, 650),
                (i * triangle_width + triangle_width / 2, 650 - triangle_height)
            ]
            pygame.draw.polygon(self.screen, color, pts)

        # fichas
        points = self.board.get_points()
        for i, p in enumerate(points):
            if p["count"] > 0:
                color = self.WHITE if p["color"] == "blanco" else self.BLACK
                for j in range(p["count"]):
                    if i < 12:
                        # fila superior (invertida visualmente)
                        x = (11 - i) * triangle_width + triangle_width / 2
                        y = triangle_height - (j * 25) - 20
                    else:
                        # fila inferior (normal)
                        x = (i - 12) * triangle_width + triangle_width / 2
                        y = 650 - triangle_height + (j * 25) + 20
                    pygame.draw.circle(self.screen, color, (int(x), int(y)), 12)
                    if self.selected_point == i:
                        pygame.draw.circle(self.screen, (255, 215, 0), (int(x), int(y)), 14, 2)

        # barra
        pygame.draw.rect(self.screen, self.DARK, (600, 0, 40, 650))
        self.draw_bar_fichas()

    def draw_bar_fichas(self):
        bx, by = 620, 325
        for j, _ in enumerate(self.board.bar_blanco):
            pygame.draw.circle(self.screen, self.WHITE, (bx, by - j * 20), 10)
        for j, _ in enumerate(self.board.bar_negro):
            pygame.draw.circle(self.screen, self.BLACK, (bx, by + j * 20), 10)

    def draw_panel(self):
        panel = pygame.Rect(780, 90, 300, 270)
        pygame.draw.rect(self.screen, (245, 245, 245), panel, border_radius=10)
        pygame.draw.rect(self.screen, self.DARK, panel, 2, border_radius=10)

        y = 110
        def line(txt):
            nonlocal y
            surf = self.FONT.render(txt, True, self.DARK)
            self.screen.blit(surf, (800, y))
            y += 28

        line(f"Turno: {self.turn.get_name()} ({self.turn.get_color()})")
        d1, d2 = self.last_roll
        line(f"Dado 1: {d1}")
        line(f"Dado 2: {d2}")
        msg = self.message
        if len(msg) > 32:
            line(msg[:32])
            line(msg[32:])
        else:
            line(msg)

    # === Clicks ===
    def get_clicked_point(self, pos):
        x, y = pos
        triangle_width = 50

        # fuera del área
        if x > 600:
            return None

        col = int(x // triangle_width)

        if y < 325:
            # fila superior: de derecha a izquierda
            return 11 - col
        else:
            # fila inferior: normal
            return 12 + col

    def cancel_selection(self):
        self.selected_point = None
        self.message = "Selección cancelada."

    # === Dados ===
    def roll_dice(self):
        self.last_roll = self.dice.roll()
        d1, d2 = self.last_roll
        self.remaining_dice = [d1, d2] if d1 != d2 else [d1, d1, d1, d1]
        self.message = f"Tiraste {d1} y {d2}. Elegí ficha para mover."
        self.awaiting_move = True
        self.selected_point = None

    # === Movimiento ===
    def handle_click(self, pos, button):
        point = self.get_clicked_point(pos)
        if button == 3:
            self.cancel_selection()
            return

        color = self.turn.get_color()
        if self.board.has_bar(color):
            ok, msg = self.board.reenter_from_bar(color, self.remaining_dice)
            self.message = msg
            if ok and self.remaining_dice:
                self.remaining_dice.pop(0)
            if not self.remaining_dice:
                self.awaiting_move = False
                self.turn = self.player2 if self.turn == self.player1 else self.player1
                self.message += " | Turno del siguiente jugador."
            return

        if point is None:
            return

        p = self.board.get_point(point)
        color_turno = self.turn.get_color()

        if self.selected_point is None:
            if p["count"] > 0 and p["color"] == color_turno:
                self.selected_point = point
                self.message = f"Origen {point} seleccionado. Dados: {self.remaining_dice}"
            else:
                self.message = "No podés mover esa ficha."
            return

        origen = self.selected_point
        destino = point
        dist = self.board.distance_in_direction(color_turno, origen, destino)

        if dist <= 0 or dist not in self.remaining_dice:
            if p["count"] > 0 and p["color"] == color_turno:
                self.selected_point = point
                self.message = f"Origen cambiado a {point}. Dados: {self.remaining_dice}"
            else:
                self.message = "Movimiento inválido para tus dados."
            return

        ok, why = self.board.can_move(origen, destino)
        if not ok:
            if p["count"] > 0 and p["color"] == color_turno:
                self.selected_point = point
                self.message = f"{why} | Origen cambiado a {point}."
            else:
                self.message = why
            return

        result = self.board.move_checker(origen, destino)
        self.message = result
        self.remaining_dice.remove(dist)
        self.selected_point = None

        if not self.remaining_dice:
            self.awaiting_move = False
            self.turn = self.player2 if self.turn == self.player1 else self.player1
            self.message += " | Turno del siguiente jugador."
        else:
            self.message += f" | Mové de nuevo (dados: {self.remaining_dice})."

    # === Loop principal ===
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
                if event.type == pygame.MOUSEBUTTONDOWN and self.awaiting_move:
                    if event.button in (1, 3):
                        self.handle_click(event.pos, event.button)

            self.draw_board()
            self.draw_panel()
            pygame.display.flip()
            clock.tick(30)


if __name__ == "__main__":
    n1, n2 = pedir_nombres()
    pygame.init()
    screen = pygame.display.set_mode((1100, 650))
    pygame.display.set_caption("Backgammon - Computación 2025")
    ui = BackgammonUI(n1, n2, screen)
    ui.run()
