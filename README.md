Trabajo Final de Computación
Proyecto: Juego de Backgammon

Alumna: María Eva Modarelli
Carrera: Ingeniería en Informática
Materia: Computación
Año: 2025

Descripción general

Este proyecto consiste en la implementación completa del juego de Backgammon en Python.
Se desarrolló una versión jugable tanto en modo texto (CLI) como con interfaz gráfica (Pygame).

El objetivo principal es aplicar los conceptos de programación orientada a objetos (POO), control de flujo, manejo de excepciones y testing automatizado, asegurando un diseño modular y mantenible.

Estructura del proyecto
backgammon/
├── core/                  # Lógica principal del juego
│   ├── board.py           # Clase Board: estructura y movimiento en el tablero
│   ├── checker.py         # Clase Checker: fichas y validaciones
│   ├── dice.py            # Clase Dice: tirada de dados
│   ├── player.py          # Clase Player: manejo de jugadores
│   └── game.py            # Clase BackgammonGame: control del flujo del juego
│
├── pygame_ui/             # Interfaz visual con Pygame
│   └── game_window.py     # Ventana principal y renderizado gráfico
│
├── cli/                   # Interfaz en consola (modo texto)
│   └── test_game.py       # Versión jugable desde terminal
│
├── tests/                 # Carpeta de tests unitarios
│   ├── test_board.py
│   ├── test_checker.py
│   ├── test_dice.py
│   ├── test_player.py
│   └── test_cli.py        # Tests del modo CLI
│
├── .coverage              # Reporte de cobertura
├── CHANGELOG.md           # Registro de cambios
├── JUSTIFICACION.md       # Explicación del diseño, clases y principios SOLID
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documento actual

Entorno virtual y dependencias

Crear entorno virtual:
python3 -m venv nombre_del_entorno
Activate entorno virtual:

source nombre_del_entorno/bin/activate     # Linux / macOS
nombre_del_entorno\Scripts\activate        # Windows


instalar dependencias:
pip install -r requirements.txt
