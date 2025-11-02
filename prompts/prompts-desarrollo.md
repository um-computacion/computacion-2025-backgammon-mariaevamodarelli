Lógica del juego (ejemplo sobre clase Board)

Modelo / herramienta usada: ChatGPT (GPT-5)
Prompt exacto:

Necesito implementar la clase Board para mi proyecto de Backgammon en Python.
El tablero debe tener 24 posiciones (puntos), y cada jugador tiene 15 fichas que deben colocarse en las posiciones iniciales estándar.
Quiero que la clase tenga métodos para obtener y mover fichas (get_points, move_checker), y que valide los movimientos según las reglas del juego.
Usá atributos con guiones bajos dobles como pide la consigna (__atributo__).
No uses Pygame ni dependencias externas, solo lógica pura.

Respuesta / resultado completo:

ChatGPT generó una clase Board con una lista de 24 puntos, cada punto almacenando color y cantidad de fichas.
Incluyó los métodos reset_starting_position(), get_points(), move_checker() y validaciones de rango (0-23) para movimientos.
Se adaptó el código para cumplir con el formato __atributo__ y se añadieron docstrings.

Uso:

Se usó como base para el archivo core/board.py, con pequeñas modificaciones en nombres de variables y mensajes de impresión.

Referencias a archivos finales:

/core/board.py


Lógica de los dados (Dice)

Modelo / herramienta usada: ChatGPT (GPT-5)
Prompt exacto:

Creá la clase Dice para el juego Backgammon en Python.
Debe permitir tirar dos dados con valores del 1 al 6 y devolver una lista con ambos valores.
Si los valores son iguales, debe duplicar la lista (por ejemplo, [3,3] → [3,3,3,3]) porque en Backgammon los dobles permiten cuatro movimientos.
Agregá docstrings y usá nombres de atributos con __.

Respuesta / resultado completo:

Se generó la clase Dice con método roll() que devuelve lista de dos valores o cuatro si son iguales.
Incluye docstring explicativo y atributo __values__.
Se integró correctamente con core/game.py y cli.py.

Uso:

Se usó directamente en /core/dice.py sin modificaciones.

Referencias a archivos finales:

/core/dice.py

# Prompts - Desarrollo

## Consulta
- **Modelo usado**: ChatGPT (GPT-5)
- **Prompt**: "¿Qué librería podría usar para que el dado sea random en Python?"

## Respuesta de la IA
La IA sugirió:
- Usar la librería estándar `random` de Python.

## Uso en el proyecto
- Se aplicó la sugerencia usando `import random`.

## Archivos impactados
- `core/dice.py`
