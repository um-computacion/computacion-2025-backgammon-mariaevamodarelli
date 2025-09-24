## justificacion
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
