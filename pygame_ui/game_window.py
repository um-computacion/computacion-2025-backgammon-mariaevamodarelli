import pygame
from core.board import Board
from core.dice import Dice
from core.player import Player
from core.game import BackgammonGame
import random

# Inicialización de PyGame
pygame.init()

# Dimensiones y ventana
WIDTH, HEIGHT = 1000, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Backgammon - Computación 2025")

# Colores
WOOD = (193, 154, 107)
DARK_WOOD = (160, 120, 80)
WHITE = (240, 240, 240)
BLACK = (20, 20, 20)
RED = (220, 40, 40)
BLUE = (30, 70, 200)
LIGHT_GRAY = (200, 200, 200)

# Fuente
FONT = pygame.font.SysFont("arial", 22)

class GameWindow:
    """Interfaz visual del Backgammon."""

    def __init__(self):
        """Inicializa jugadores, tablero, dados y lógica principal."""
        self.board = Board()
        self.dice = Dice()
        self.player1 = Player("Eva", "blanco")
        self.player2 = Player("Carla", "negro")
        self.game = BackgammonGame(self.player1, self.player2, self.board, self.dice)
        self.running = True
        self.turn = self.player1

    def draw_board(self):
        """Dibuja el tablero con triángulos alternados."""
        SCREEN.fill(WOOD)

        board_rect = pygame.Rect(100, 50, 800, 600)
        pygame.draw.rect(SCREEN, DARK_WOOD, board_rect, border_radius=12)

        triangle_width = 800 // 12
        triangle_height = 250

        # Parte superior
        for i in range(12):
            color = RED if i % 2 == 0 else LIGHT_GRAY
            x = 100 + i * triangle_width
            points = [(x, 50), (x + triangle_width, 50), (x + triangle_width // 2, 50 + triangle_height)]
            pygame.draw.polygon(SCREEN, color, points)

        # Parte inferior (invertidos)
        for i in range(12):
            color = BLUE if i % 2 == 0 else LIGHT_GRAY
            x = 100 + i * triangle_width
            points = [(x, 650), (x + triangle_width, 650), (x + triangle_width // 2, 650 - triangle_height)]
            pygame.draw.polygon(SCREEN, color, points)

        pygame.draw.line(SCREEN, BLACK, (WIDTH // 2, 50), (WIDTH // 2, 650), 4)

    def draw_checkers(self):
        """Dibuja las fichas según la posición inicial del tablero."""
        points = self.board.get_points()
        triangle_width = 800 // 12
        for i, p in enumerate(points):
            if p["count"] > 0:
                color = WHITE if p["color"] == "blanco" else BLACK
                # Coordenadas base
                if i < 12:
                    x = 100 + i * triangle_width + triangle_width // 2
                    y_start = 50 + 25
                    for j in range(p["count"]):
                        y = y_start + j * 30
                        pygame.draw.circle(SCREEN, color, (x, y), 15)
                        pygame.draw.circle(SCREEN, BLACK, (x, y), 15, 2)
                else:
                    x = 100 + (23 - i) * triangle_width + triangle_width // 2
                    y_start = 650 - 25
                    for j in range(p["count"]):
                        y = y_start - j * 30
                        pygame.draw.circle(SCREEN, color, (x, y), 15)
                        pygame.draw.circle(SCREEN, BLACK, (x, y), 15, 2)

    def draw_dice(self):
        """Dibuja los dados en pantalla."""
        d1, d2 = self.dice.get_last_roll()
        dice_rect1 = pygame.Rect(880, 200, 50, 50)
        dice_rect2 = pygame.Rect(940, 200, 50, 50)
        pygame.draw.rect(SCREEN, WHITE, dice_rect1, border_radius=8)
        pygame.draw.rect(SCREEN, WHITE, dice_rect2, border_radius=8)
        pygame.draw.rect(SCREEN, BLACK, dice_rect1, 2, border_radius=8)
        pygame.draw.rect(SCREEN, BLACK, dice_rect2, 2, border_radius=8)

        text1 = FONT.render(str(d1), True, BLACK)
        text2 = FONT.render(str(d2), True, BLACK)
        SCREEN.blit(text1, (dice_rect1.centerx - 7, dice_rect1.centery - 10))
        SCREEN.blit(text2, (dice_rect2.centerx - 7, dice_rect2.centery - 10))

        msg = FONT.render("Presioná ESPACIO para tirar los dados", True, BLACK)
        SCREEN.blit(msg, (760, 270))

    def draw_turn(self):
        """Muestra el turno actual."""
        turn_text = FONT.render(f"Turno: {self.turn.get_name()} ({self.turn.get_color()})", True, BLACK)
        SCREEN.blit(turn_text, (760, 150))

    def update(self):
        """Actualiza la pantalla."""
        pygame.display.flip()

    def run(self):
        """Bucle principal del juego."""
        self.game.start_game()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dice.roll()  # tirar dados
                        # alternar turno
                        self.turn = self.player2 if self.turn == self.player1 else self.player1

            self.draw_board()
            self.draw_checkers()
            self.draw_turn()
            self.draw_dice()
            self.update()

        pygame.quit()


if __name__ == "__main__":
    GameWindow().run()
