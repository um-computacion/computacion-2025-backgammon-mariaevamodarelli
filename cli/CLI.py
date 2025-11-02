import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.board import Board
from core.dice import Dice
from core.player import Player
from core.game import BackgammonGame


def render_board_counts(board):
    """Muestra las 24 posiciones con color y cantidad de fichas."""
    pts = board.get_points()
    filas = []
    for i, p in enumerate(pts):
        color = p["color"][0].upper() if p["color"] in ("blanco", "negro") else "-"
        filas.append(f"{i:02d}:{color}{p['count']}")
    print("SUP:", " ".join(filas[:12]))
    print("INF:", " ".join(filas[12:]))


def pedir_movimiento(color, dice_values):
    """Pide al jugador que elija origen, destino y qué dado usar."""
    print(f"\nDados disponibles: {dice_values}")
    while True:
        try:
            origen = int(input("Elegí el punto de origen (0-23): "))
            destino = int(input("Elegí el punto de destino (0-23): "))
            if origen < 0 or origen > 23 or destino < 0 or destino > 23:
                print("Los puntos deben estar entre 0 y 23.")
                continue
            return origen, destino
        except ValueError:
            print("Ingresá solo números válidos.")


def main():
    print("=== Backgammon (Interfaz CLI Jugable) ===")
    name1 = input("Nombre J1 (blanco): ").strip() or "Jugador 1"
    name2 = input("Nombre J2 (negro): ").strip() or "Jugador 2"

    board = Board()
    dice = Dice()
    p1 = Player(name1, "blanco")
    p2 = Player(name2, "negro")
    game = BackgammonGame(p1, p2, board, dice)

    board.reset_starting_position()
    turn = p1

    while True:
        print("\n---------------------------------------")
        print(f"Turno de {turn.get_name()} ({turn.get_color()})")
        render_board_counts(board)

        cmd = input("[Enter] tirar dados | q salir: ").strip().lower()
        if cmd == "q":
            print("Fin del juego.")
            break

        d1, d2 = dice.roll()
        print(f"Dados: {d1} y {d2}")
        dados = [d1, d2]

        movimientos_restantes = 2
        while movimientos_restantes > 0:
            origen, destino = pedir_movimiento(turn.get_color(), dados)
            resultado = board.move_checker(origen, destino)
            print(f"  {resultado}")
            render_board_counts(board)

            movimientos_restantes -= 1
            if movimientos_restantes > 0:
                seguir = input("¿Querés hacer otro movimiento? (s/n): ").strip().lower()
                if seguir != "s":
                    break

        # cambiar turno
        turn = p2 if turn == p1 else p1


if __name__ == "__main__":
    main()
