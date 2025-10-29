# Justificación

Arranqué por la lógica en `core/`. La primera clase implementada es `Dice` porque es independiente del resto y me permite empezar a testear rápido.  

## Clase Dice
- **Atributo `__last_roll__`**: se mantiene como tupla `(d1, d2)` para registrar la última tirada.  
- **Método `roll()`**: usa `random.randint(1, 6)` para simular el lanzamiento de dos dados.  
- **Método `is_double()`**: agregado porque en Backgammon una tirada doble permite movimientos adicionales, y tener un método que lo detecte facilita la lógica.  
- **Tests**: se validan inicialización, tiradas válidas, actualización del estado interno y casos de tiradas dobles.

## Clase Player
- **Atributos privados (`__name__`, `__color__`, `__checkers__`)**: definidos siguiendo la consigna de prefijo `__`.  
- **Getters y setters**: se usan para encapsular la lógica y validar entradas.  
  - `set_name` y `set_color`: validan que no sean vacíos o solo espacios.  
  - `set_checkers`: valida que la cantidad de fichas sea un entero entre 0 y 15 (cada jugador comienza con 15 fichas y nunca puede tener más).  
- **Justificación**: con setters que validan se asegura consistencia de los objetos y se evitan estados inválidos.  
- **Tests**: cubren inicialización, cambios de nombre y color, validaciones de entradas inválidas y límite de 15 fichas.

## Clase Board
- **Atributo `__points__`**: lista de 24 posiciones que representan los puntos del tablero de Backgammon.  
- **Getters y setters de puntos**: verifican que el índice esté entre 0 y 23 y que la cantidad de fichas sea un entero no negativo, evitando estados inválidos en el tablero.  
- **Método `reset_starting_position()`**: inicializa el tablero con la distribución estándar de Backgammon (dos fichas en el punto 24, cinco en el 13, tres en el 8, cinco en el 6, y la distribución espejo para el otro jugador). Se decidió guardar solamente las cantidades, sin distinguir colores aún, para simplificar la lógica inicial.  
- **Justificación**: el uso de una lista fija de 24 posiciones hace más simple modelar el tablero y manejar validaciones de rango. La inicialización permite empezar a probar jugadas más adelante.  
- **Tests**: verifican que el tablero arranca con 24 posiciones, que las posiciones clave se inicializan correctamente, que el total de fichas es 30 (15 por jugador) y que los índices inválidos lanzan `ValueError`.

### Métodos adicionales de Board
- **`get_total_checkers()`**: permite verificar rápidamente el total de fichas sobre el tablero.  
- **`clear_board()`** y **`reset_board()`**: vacían el tablero dejando las 24 posiciones en cero, útiles para reiniciar una partida.  
- **`is_empty()`**: devuelve `True` si el tablero no tiene fichas, lo cual facilita validar estados iniciales o finales.  
- **`get_non_empty_points()`**: devuelve los índices de los puntos que tienen fichas, para recorrer solo las posiciones activas.  
- **`has_checkers_at(index)`**: indica si un punto específico tiene fichas, evitando leer directamente la lista interna.  
- **`move_checkers(from_idx, to_idx, n)`**: implementa la lógica básica de mover fichas entre puntos del tablero, validando índices y cantidad.  

Estos métodos amplían la funcionalidad de la clase `Board` sin modificar su estructura central. Sirven como utilidades para validar estados del tablero y preparar la lógica del juego más adelante.  
- **Tests**: se agregaron pruebas unitarias para cada nuevo método verificando su comportamiento esperado y la detección de errores en casos inválidos.

## Clase BackgammonGame## Clase BackgammonGame
- **Propósito**: orquestar las piezas del juego sin mezclar responsabilidades. La lógica de dados, tablero y jugadores se mantiene en sus clases; `BackgammonGame` solo las integra.
- **Diseño**: el constructor recibe `player1`, `player2`, `board` y `dice`. Se exponen getters simples (`get_player1`, `get_player2`, `get_board`, `get_dice`) para acceder a los componentes cuando se necesiten.
- **Justificación**: separar la orquestación del estado evita acoplar reglas de juego dentro de `Board`, `Dice` o `Player`. Esto facilita testear cada parte por separado y permite evolucionar reglas (turnos, movimientos válidos, etc.) más adelante.
- **Tests**: se prueba que al crear `BackgammonGame` con instancias reales de `Player`, `Board` y `Dice`, los getters devuelven exactamente las mismas referencias (inyección de dependencias).

### Método start_game()
- **Propósito**: preparar el inicio de la partida combinando los componentes principales.
  Llama a `reset_starting_position()` del `Board` para dejar el tablero en la posición inicial
  y a `roll()` de `Dice` para realizar la primera tirada.
- **Justificación**: este método centraliza el proceso de inicio sin mezclar responsabilidades.
  Permite que la clase `BackgammonGame` coordine las otras clases sin modificar su lógica interna.
  De esta forma, se conserva la separación de responsabilidades y se facilita la extensión futura
  (por ejemplo, manejar turnos o verificar quién empieza).
- **Tests**: se validó que el tablero quede con 30 fichas (15 por jugador) y que la primera tirada
  devuelva dos valores entre 1 y 6.

### Método restart_game()
- **Propósito**: reiniciar una partida sin necesidad de crear nuevos objetos. 
  Limpia el tablero, vuelve a dejar las fichas en la posición inicial y lanza los dados nuevamente.  
- **Justificación**: este método simplifica el reinicio del juego, evitando repetir pasos manuales
  o crear instancias nuevas de las clases principales. Es útil para pruebas, reinicios o nuevas rondas.  
- **Tests**: se comprobó que, tras llamar a `restart_game()`, el tablero queda nuevamente con
  30 fichas (15 por jugador) y se genera una nueva tirada de dados válida.

### Método end_game()
- **Propósito**: indicar el final de la partida y limpiar los estados relacionados, 
  en este caso la última tirada de dados.  
- **Justificación**: al mantener un atributo interno `__game_over__` se puede 
  controlar desde la clase principal si la partida sigue o no, 
  sin necesidad de eliminar las instancias de `Board`, `Dice` o `Player`.  
- **Tests**: se verifica que al finalizar el juego, el atributo `__game_over__` 
  quede en `True`, que los dados se reinicien a `(0, 0)` y que el método 
  devuelva el mensaje `"Juego finalizado"`.

## Interfaz gráfica con PyGame

### Objetivo
Agregar una interfaz mínima pero funcional para **visualizar** el backgammon, **tirar los dados** y **ver el turno** de cada jugador, reutilizando toda la lógica existente en `core/` sin duplicar reglas dentro de la UI.

### Decisiones de diseño
- **Separación de responsabilidades**: la UI vive en `pygame_ui/game_window.py`. La lógica del juego (tablero, jugadores, dados) sigue en `core/`.
- **Estructura del tablero**: `Board` representa 24 puntos (0..23). Para poder dibujar fichas de cada color, cada punto guarda un diccionario con `{"count": n, "color": "blanco"|"negro"|None}`.
- **Mapeo visual**:
  - 12 triángulos arriba (izq→der) y 12 abajo (der→izq) para simular el tablero real.
  - Las fichas se dibujan como círculos (blanco/negro) apilados desde el borde.
- **Flujo de inicio**: `BackgammonGame.start_game()` reinicia posiciones y hace una primera tirada. La UI la muestra junto con el **turno actual**.
- **Interacción**:
  - **ESPACIO**: tira los dados y alterna el turno (visual). Por ahora no mueve fichas; la UI sólo refleja estado.
  - Cierre de ventana con el evento estándar de PyGame.

### Qué se ve en pantalla
- Tablero con triángulos alternados (superior rojo/gris, inferior azul/gris).
- Fichas iniciales colocadas según `Board.reset_starting_position()`.
- Panel lateral con **Turno: Nombre (color)** y los **dos dados**.
- Mensaje “Presioná ESPACIO para tirar los dados”.

### Limitaciones actuales (plan de mejora inmediato)
- **Las fichas no se mueven** aún: falta conectar clicks con `BackgammonGame.move_checker(...)`.
- **Texto superpuesto** con el tablero en algunas resoluciones: se agregará un panel lateral opaco para mejorar legibilidad.
- **Varias tiradas seguidas**: se limitará a una tirada por turno con una bandera `can_roll` en la UI.

### Justificación de cambios en `core/`
- `Board` pasó de una lista de enteros a una lista de diccionarios `{count, color}` para permitir:
  - Dibujado por color en la UI.
  - Reglas futuras (bloqueos, “comer”, bearing off) sin hacks visuales.
- Se mantuvo la **API pública** de getters para no romper tests existentes y facilitar la transición.

