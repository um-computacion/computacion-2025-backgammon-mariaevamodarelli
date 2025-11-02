# Justificación del Diseño

## Resumen del Diseño General

El proyecto Backgammon se estructura en dos capas principales:
- **`core/`**: contiene toda la lógica del juego (reglas, validaciones, estado).
- **`pygame_ui/`**: interfaz gráfica que consume la lógica sin duplicarla.

Esta separación permite testear la lógica sin dependencias gráficas y facilita agregar nuevas interfaces (CLI, web) sin modificar reglas del juego.

## Clases Principales

### Dice
- **Responsabilidad**: manejar tiradas de dados.
- **Atributo `__last_roll__`**: tupla `(d1, d2)` que registra la última tirada.
- **Método `is_double()`**: detecta tiradas dobles (importante en Backgammon para movimientos adicionales).
- **Justificación**: clase independiente y simple, ideal para comenzar el desarrollo y establecer patrones de testing.

### Player
- **Responsabilidad**: almacenar información del jugador.
- **Atributos**: `__name__`, `__color__`, `__checkers__` (todos privados según requisitos).
- **Validaciones en setters**:
  - Nombres y colores no pueden ser vacíos.
  - Cantidad de fichas debe estar entre 0 y 15.
- **Justificación**: encapsulación mediante getters/setters evita estados inválidos.

### Checker
- **Responsabilidad**: representar una ficha individual.
- **Atributo `__color__`**: solo acepta "blanco" o "negro".
- **Justificación**: aunque simple, mantener una clase separada respeta Single Responsibility y facilita extensiones futuras.

### Board
- **Responsabilidad**: gestionar el tablero y validar movimientos.
- **Estructura de datos**: lista de 24 diccionarios `{"count": n, "color": str|None}`.
  - Decisión tomada para soportar colores sin estructuras auxiliares complejas.
  - Alternativas descartadas: lista de enteros (no guarda color), clases Point (overhead innecesario).
- **Atributos adicionales**: `__bar_blanco__`, `__bar_negro__`, `__bearoff_blanco__`, `__bearoff_negro__`.

#### Métodos clave de Board

**`distance_in_direction(color, from_idx, to_idx)`**
- Calcula distancia de movimiento según dirección correcta:
  - Blanco (antihorario): `to_idx - from_idx` (0→23).
  - Negro (horario): `from_idx - to_idx` (23→0).
- Justificación: centraliza lógica de dirección evitando duplicación y errores.

**`can_move(from_idx, to_idx)`**
- Valida movimiento sin ejecutarlo.
- Retorna tupla `(bool, mensaje)` para feedback al usuario.
- Justificación: separar validación de ejecución facilita UI y testing.

**`move_checker(from_idx, to_idx)`**
- Ejecuta movimiento validado.
- Implementa captura de fichas (envío al bar).
- Maneja bear off (sacar fichas del tablero).
- Justificación: concentra toda la lógica de modificación del tablero en un lugar.

**`reenter_from_bar(color, dice_values)`**
- Reingresa fichas capturadas según valores de dados.
- Blancas: puntos 0-5, negras: puntos 18-23.
- Justificación: regla obligatoria de Backgammon (no se puede mover hasta salir del bar).

### BackgammonGame
- **Responsabilidad**: orquestar componentes sin implementar reglas específicas.
- **Patrón**: inyección de dependencias (recibe `player1`, `player2`, `board`, `dice` por constructor).
- **Métodos principales**:
  - `start_game()`: inicializa tablero y primera tirada.
  - `restart_game()`: reinicia partida sin crear nuevos objetos.
  - `end_game()`: marca finalización y limpia estado.
  - `move_checker(player, from, to)`: valida jugador y delega a Board.
- **Justificación**: mantiene lógica de juego separada de componentes individuales, facilita testing con mocks.

### BackgammonUI
- **Responsabilidad**: renderizar y capturar input del usuario.
- **Ubicación**: `pygame_ui/game_window.py` (separado de `core/`).
- **Componentes visuales**:
  - Tablero: 24 triángulos (12 superiores, 12 inferiores) con fichas apiladas.
  - Bar central: muestra fichas capturadas.
  - Panel lateral: turno, dados, mensajes, instrucciones.
- **Interacción**: ESPACIO para dados, clicks para mover, click derecho para cancelar.
- **Justificación**: UI consume APIs públicas de `core/` sin duplicar lógica, permite agregar otras interfaces fácilmente.

## Decisiones de Diseño Relevantes

### 1. Direcciones de movimiento (corrección aplicada)
**Problema inicial**: fichas se movían en direcciones invertidas.

**Solución**: 
- Invertir fórmulas en `distance_in_direction()`.
- Ajustar validaciones en `move_checker()`.

**Por qué falló antes**: confusión entre índices visuales y lógicos del tablero.

### 2. Validación separada de ejecución
**Decisión**: `can_move()` valida, `move_checker()` ejecuta.

**Por qué**: UI puede preguntar "¿es válido?" sin modificar estado, facilita debugging y testing.

### 3. Panel de información mejorado
**Cambios aplicados**:
- Tamaño: 330x500px (antes 300x270px).
- Tipografía: 18-28pt (antes 14-26pt).
- Dados visuales: 40x40px como cubos.
- Sección "Disponibles" para dados restantes.

**Por qué**: legibilidad era insuficiente, usuarios reportaban dificultad para leer información.

## Excepciones y Manejo de Errores

### Estrategia
- **ValueError** para entradas inválidas (nombres vacíos, índices fuera de rango, valores fuera de límites).
- **Mensajes descriptivos** en validaciones de movimiento (retornos en vez de excepciones).

### Ejemplos por clase
- **Dice**: `set_last_roll()` lanza `ValueError` si no es tupla válida.
- **Player**: setters lanzan `ValueError` si validaciones fallan.
- **Checker**: `__init__` lanza `ValueError` si color no es "blanco" o "negro".
- **Board**: `can_move()` retorna `(False, mensaje)` en vez de lanzar excepción (mejor para UI).

### Justificación
- Excepciones para errores de programación (bugs).
- Retornos con mensajes para errores de usuario (jugadas inválidas).
- Facilita mostrar feedback sin try-catch excesivos.

## Estrategia de Testing

### Herramientas
- **pytest**: framework principal.
- **pytest-cov**: medición de cobertura.
- **GitHub Actions**: CI/CD automático.
- **SonarCloud**: análisis de calidad.

### Cobertura
- **Objetivo**: 90%+ según requisitos.
- **Estado actual**: [indicar porcentaje]
- **Prioridad**: lógica crítica (movimientos, validaciones) con 100%.

### Tipos de tests
- **Unitarios**: cada clase aislada (Dice, Player, Checker, Board).
- **Integración**: BackgammonGame coordinando componentes.
- **Casos cubiertos**: inicialización, validaciones, casos borde, excepciones.

## Cumplimiento de SOLID

### Single Responsibility
✅ Cada clase tiene una única responsabilidad:
- Dice: solo dados.
- Player: solo información de jugador.
- Board: solo tablero y validaciones.
- BackgammonGame: solo orquestación.
- BackgammonUI: solo renderizado.

### Open/Closed
✅ Clases diseñadas para extenderse sin modificar:
- Agregar nuevas UIs sin tocar `core/`.
- Agregar variantes de juego extendiendo clases base.

### Liskov Substitution
✅ No hay herencia compleja (diseño basado en composición).

### Interface Segregation
✅ Interfaces mínimas: cada clase expone solo lo necesario.

### Dependency Inversion
✅ BackgammonGame recibe dependencias por constructor (inyección).
✅ UI depende de abstracciones (APIs públicas) no de detalles.

## Diagrama de Clases Simplificado
```
┌──────────────────┐
│ BackgammonGame   │
│ (Orquestador)    │
└────────┬─────────┘
         │
    ┌────┴─────┬────────┬────────┐
    │          │        │        │
    ▼          ▼        ▼        ▼
┌─────────┐ ┌──────┐ ┌────────┐ ┌────────┐
│ Player  │ │ Dice │ │ Board  │ │Checker │
│ (x2)    │ │      │ │        │ │        │
└─────────┘ └──────┘ └────────┘ └────────┘
                          │
                          │ usa (concepto)
                          │
                          ▼
                     ┌─────────────┐
                     │BackgammonUI │
                     │ (Interfaz)  │
                     └─────────────┘
```

## Evolución del Proyecto

### Sprint 1
- Estructura base, Dice, Player, Checker.
- Tests unitarios, CI/CD.

### Sprint 2
- Board con lógica completa, BackgammonGame.
- Tests de integración.

### Sprint 3 (actual)
- Interfaz gráfica funcional.
- Corrección de direcciones de movimiento.
- Panel mejorado visualmente.
- Captura y bar implementados.

### Próximos pasos
- Bear off completo.
- Detección de victoria.
- CLI funcional.
- Persistencia Redis (opcional).

## Pendientes Conocidos

- [ ] Bear off con todas las validaciones.
- [ ] Detectar condición de victoria.
- [ ] Validar jugadas imposibles (sin movimientos válidos).
- [ ] CLI completamente funcional.
- [ ] Consolidar lógica duplicada entre Game y Board.

## Referencias

- Reglas: https://es.wikipedia.org/wiki/Backgammon
- Pygame: https://www.pygame.org/docs/
- Docstrings: https://realpython.com/documenting-python-code/
- Keep a Changelog: https://keepachangelog.com/en/1.1.0/
- Juego de referencia: https://www.ludoteka.com/clasika/backgammon-es.html