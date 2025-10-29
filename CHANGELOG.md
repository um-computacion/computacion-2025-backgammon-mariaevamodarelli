# Changelog
Todas las modificaciones notables de este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Added
- Clase `Dice` con `__init__`, `roll()`, getters y setters.
- Tests iniciales de `Dice`.
- Documento `JUSTIFICACION.md`.
- Documento `CHANGELOG.md` (estructura inicial).
- Estructura base del proyecto (`core/`, `cli/`, `tests/`).
- Configuración inicial de GitHub Actions + SonarCloud.
- Método `is_double()` en `Dice` y sus tests (#8).
- Validación en `Player` para un máximo de 15 fichas (#15).
- Métodos `get/set_checkers` en `Player` y sus tests (#15).
- Validaciones en `set_name` y `set_color` en `Player` (#15).
- Métodos `get_name` y `set_name` en `Player` y sus tests (#15).
- Métodos `get_color` y `set_color` en `Player` y sus tests (#15).
- Clase `Board` inicializada con 24 posiciones vacías (#29).
- Método `reset_starting_position()` en `Board` y sus tests (#29).
- Método `get_total_checkers()` en `Board` y su test.
- Método `clear_board()` en `Board` y su test.
- Método `is_empty()` en `Board` y sus tests.
- Método `get_non_empty_points()` en `Board` y su test.
- Método `has_checkers_at()` en `Board` y sus tests.
- Método `move_checkers()` en `Board` y su test.
- Método `reset_board()` en `Board` y su test.
- Clase `BackgammonGame` con getters básicos (`get_player1`, `get_player2`, `get_board`, `get_dice`).
- Tests de `BackgammonGame` para inicialización y getters.
- Método `start_game()` en `BackgammonGame`:
  reinicia el tablero con la disposición inicial y realiza la primera tirada de dados.
- Tests de `BackgammonGame.start_game()` que verifican la reinicialización del tablero
  y la validez de la tirada de dados.
- Método `restart_game()` en `BackgammonGame`:
  reinicia el tablero, restablece la posición inicial y realiza una nueva tirada de dados.
- Tests de `BackgammonGame.restart_game()` que verifican la reinicialización del tablero
  y la nueva tirada de dados.
- Método `end_game()` en `BackgammonGame`: 
  marca la partida como finalizada y limpia la última tirada de dados.
- Tests de `BackgammonGame.end_game()` que verifican el estado `__game_over__`
  y la limpieza de los dados.
- Carpeta `pygame_ui/` con `game_window.py` para la interfaz PyGame.
- Render del tablero con 24 triángulos (12 arriba, 12 abajo) y apilado de fichas por punto.
- HUD lateral con **turno actual** y **dados**; tecla **ESPACIO** para tirar y alternar turno.
- Integración de UI con `BackgammonGame.start_game()` y `Dice`.

### Changed
- Algunos tests de `Dice` actualizados para mejorar cobertura.
- Ajustes en reportes automáticos de cobertura y pylint.
- `Board`: ahora cada punto es un diccionario `{"count": n, "color": ...}` para soportar color de fichas en la UI y reglas futuras.


### Fixed
- Arreglos en reportes generados por GitHub Actions.
- Limpieza de archivos de reportes innecesarios del repositorio.
