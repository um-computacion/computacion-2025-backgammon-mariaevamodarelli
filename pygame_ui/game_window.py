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
        self.GOLD = (255, 215, 0)
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
                    pygame.draw.circle(self.screen, (80, 80, 80), (int(x), int(y)), 12, 1)
                    
                    if self.selected_point == i:
                        pygame.draw.circle(self.screen, self.GOLD, (int(x), int(y)), 15, 3)

        # BAR CENTRAL
        pygame.draw.rect(self.screen, (210, 180, 140), (300, 0, 10, 650))
        
        # Bear off zones
        pygame.draw.rect(self.screen, (210, 180, 140), (600, 325, 40, 325))
        pygame.draw.rect(self.screen, (210, 180, 140), (600, 0, 40, 325))
        self.draw_bar_fichas()

    def draw_bar_fichas(self):
        bar_x = 305
        bar_y_center = 325
        
        # Fichas blancas en el bar
        for i in range(len(self.board.__bar_blanco__)):
            y = bar_y_center + (i * 25) + 20
            pygame.draw.circle(self.screen, self.WHITE, (bar_x, y), 12)
            pygame.draw.circle(self.screen, (80, 80, 80), (bar_x, y), 12, 1)
        
        # Fichas negras en el bar
        for i in range(len(self.board.__bar_negro__)):
            y = bar_y_center - (i * 25) - 20
            pygame.draw.circle(self.screen, self.BLACK, (bar_x, y), 12)
            pygame.draw.circle(self.screen, (80, 80, 80), (bar_x, y), 12, 1)


    def draw_panel(self):
        # Panel principal con sombra (más grande)
        shadow = pygame.Rect(755, 75, 330, 500)
        pygame.draw.rect(self.screen, (180, 180, 180), shadow, border_radius=12)
        
        panel = pygame.Rect(750, 70, 330, 500)
        pygame.draw.rect(self.screen, (255, 255, 255), panel, border_radius=12)
        pygame.draw.rect(self.screen, (100, 100, 100), panel, 3, border_radius=12)

        # Título del panel
        title_font = pygame.font.SysFont("arial", 26, bold=True)
        title = title_font.render("INFORMACIÓN", True, self.DARK)
        self.screen.blit(title, (820, 105))
        
        # Línea separadora
        pygame.draw.line(self.screen, (200, 200, 200), (800, 140), (1060, 140), 2)

        # Información del turno con color
        y = 155
        turn_font = pygame.font.SysFont("arial", 20, bold=True)
        label_font = pygame.font.SysFont("arial", 18)
        value_font = pygame.font.SysFont("arial", 18, bold=True)
        
        # Turno actual
        turn_label = label_font.render("Turno:", True, (80, 80, 80))
        self.screen.blit(turn_label, (800, y))
        
        player_name = self.turn.get_name()
        player_color = self.turn.get_color()
        color_display = self.WHITE if player_color == "blanco" else self.BLACK
        
        # Círculo indicador del color
        pygame.draw.circle(self.screen, color_display, (870, y + 10), 8)
        pygame.draw.circle(self.screen, (100, 100, 100), (870, y + 10), 8, 2)
        
        player_text = turn_font.render(f"{player_name}", True, self.DARK)
        self.screen.blit(player_text, (890, y))
        
        y += 40
        
        # Dados
        d1, d2 = self.last_roll
        dice_label = label_font.render("Dados:", True, (80, 80, 80))
        self.screen.blit(dice_label, (800, y))
        
        # Dibujar dados como cubos
        dice_size = 35
        dice_x = 880
        
        # Dado 1
        dice_rect1 = pygame.Rect(dice_x, y - 5, dice_size, dice_size)
        pygame.draw.rect(self.screen, self.WHITE, dice_rect1, border_radius=5)
        pygame.draw.rect(self.screen, self.DARK, dice_rect1, 2, border_radius=5)
        dice_val1 = value_font.render(str(d1), True, self.DARK)
        self.screen.blit(dice_val1, (dice_x + 12, y))
        
        # Dado 2
        dice_rect2 = pygame.Rect(dice_x + 50, y - 5, dice_size, dice_size)
        pygame.draw.rect(self.screen, self.WHITE, dice_rect2, border_radius=5)
        pygame.draw.rect(self.screen, self.DARK, dice_rect2, 2, border_radius=5)
        dice_val2 = value_font.render(str(d2), True, self.DARK)
        self.screen.blit(dice_val2, (dice_x + 62, y))
        
        y += 50
        
        # Dados restantes
        if self.remaining_dice:
            remaining_label = label_font.render("Disponibles:", True, (80, 80, 80))
            self.screen.blit(remaining_label, (800, y))
            
            remaining_text = value_font.render(str(self.remaining_dice), True, (0, 120, 0))
            self.screen.blit(remaining_text, (920, y))
            y += 35
        
        # Línea separadora
        pygame.draw.line(self.screen, (200, 200, 200), (800, y), (1060, y), 1)
        y += 15
        
        # Mensaje con wrap mejorado
        msg = self.message
        msg_font = pygame.font.SysFont("arial", 16)
        max_width = 250
        words = msg.split()
        lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + word + " "
            if msg_font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word + " "
        if current_line:
            lines.append(current_line)
        
        for line in lines[:3]:  # Máximo 3 líneas
            msg_surf = msg_font.render(line.strip(), True, (50, 50, 50))
            self.screen.blit(msg_surf, (800, y))
            y += 22
        
        # Instrucciones al pie
        y = 320
        pygame.draw.line(self.screen, (200, 200, 200), (800, y), (1060, y), 1)
        y += 10
        
        help_font = pygame.font.SysFont("arial", 14, italic=True)
        help1 = help_font.render("ESPACIO: Tirar dados", True, (100, 100, 100))
        help2 = help_font.render("Click derecho: Cancelar", True, (100, 100, 100))
        self.screen.blit(help1, (800, y))
        self.screen.blit(help2, (800, y + 20))
    
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
        if dist < 0:
            dist = abs(dist)

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