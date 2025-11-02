# Changelog

Todas las modificaciones notables de este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Added
- Clase `Dice` con `__init__`, `roll()`, getters y setters.
- Tests iniciales de `Dice` con cobertura completa.
- Documento `JUSTIFICACION.md` con diseño y decisiones arquitectónicas.
- Documento `CHANGELOG.md` (estructura inicial).
- Estructura base del proyecto (`core/`, `cli/`, `pygame_ui/`, `tests/`).
- Configuración inicial de GitHub Actions + SonarCloud para CI/CD.
- Archivo `requirements.txt` con dependencias del proyecto (pygame, pytest, pytest-cov).
- Método `is_double()` en `Dice` para detectar tiradas dobles (#8).
- Tests de `is_double()` verificando casos de dobles y no dobles.
- Clase `Player` con atributos privados `__name__`, `__color__`, `__checkers__`.
- Validación en `Player` para un máximo de 15 fichas (#15).
- Métodos `get_checkers()` y `set_checkers()` en `Player` con validación 0-15 (#15).
- Validaciones en `set_name()` y `set_color()` en `Player` (#15).
- Métodos `get_name()` y `set_name()` en `Player` con tests (#15).
- Métodos `get_color()` y `set_color()` en `Player` con tests (#15).
- Tests completos de `Player` cubriendo inicialización y validaciones.
- Clase `Checker` para representar fichas individuales.
- Validación de color en `Checker` (solo "blanco" o "negro").
- Tests de `Checker` verificando inicialización y rechazo de colores inválidos.
- Clase `Board` inicializada con 24 posiciones representadas como diccionarios (#29).
- Estructura de puntos: `{"count": n, "color": str|None}` para soporte de colores.
- Atributos `__bar_blanco__` y `__bar_negro__` para fichas capturadas.
- Atributos `__bearoff_blanco__` y `__bearoff_negro__` para fichas fuera del tablero.
- Método `reset_starting_position()` en `Board` con distribución estándar de Backgammon (#29).
- Tests de `reset_starting_position()` verificando 30 fichas totales y posiciones correctas.
- Método `get_total_checkers()` en `Board` para contar fichas activas.
- Método `clear_board()` en `Board` para vaciar todas las posiciones.
- Método `reset_board()` en `Board` como alias de `clear_board()`.
- Método `is_empty()` en `Board` para verificar tablero vacío.
- Método `get_non_empty_points()` en `Board` para listar puntos con fichas.
- Método `has_checkers_at(index)` en `Board` para verificar presencia de fichas.
- Método `distance_in_direction(color, from_idx, to_idx)` para cálculo de distancia según color.
- Método `can_move(from_idx, to_idx)` en `Board` para validar movimientos sin efectos secundarios.
- Método `move_checker(from_idx, to_idx)` en `Board` para ejecutar movimientos validados.
- Lógica de captura de fichas: envío automático al bar al comer ficha enemiga solitaria.
- Método `has_bar(color)` en `Board` para verificar fichas capturadas.
- Método `reenter_from_bar(color, dice_values)` para reingresar fichas desde el bar.
- Tests completos de `Board` cubriendo movimientos, captura, bar y validaciones.
- Clase `BackgammonGame` como orquestador principal del juego.
- Getters básicos en `BackgammonGame`: `get_player1()`, `get_player2()`, `get_board()`, `get_dice()`.
- Atributo `__game_over__` en `BackgammonGame` para controlar estado de finalización.
- Tests de `BackgammonGame` para inicialización y getters.
- Método `start_game()` en `BackgammonGame`: reinicia tablero y realiza primera tirada.
- Tests de `start_game()` verificando inicialización correcta y tirada válida.
- Método `restart_game()` en `BackgammonGame`: reinicia partida completa con nueva tirada.
- Tests de `restart_game()` verificando reset de tablero y nuevos dados.
- Método `end_game()` en `BackgammonGame`: marca partida como finalizada y limpia dados.
- Tests de `end_game()` verificando estado `__game_over__` y limpieza.
- Método `move_checker(player, from_point, to_point)` en `BackgammonGame` con validaciones de jugador.
- Carpeta `pygame_ui/` con módulo `game_window.py` para interfaz gráfica.
- Clase `BackgammonUI` manejando renderizado y eventos de Pygame.
- Renderizado del tablero con 24 triángulos (12 superiores rojos/grises, 12 inferiores azules/grises).
- Apilado visual de fichas con círculos de 12px y separación de 25px.
- Barra central (x=300) para visualizar fichas capturadas en el bar.
- Zonas de bear off (x=600) para fichas que salen del tablero.
- Panel de información lateral (330x500px) con diseño mejorado.
- Título "INFORMACIÓN" en 28pt bold en el panel.
- Sección de turno con círculo indicador de color (10px) y nombre del jugador (22pt).
- Visualización de dados como cubos de 40x40px con valores en 20pt bold.
- Sección "Disponibles" mostrando lista de dados restantes por usar.
- Área de mensajes con word-wrap automático (hasta 4 líneas, 18pt).
- Instrucciones de ayuda al pie del panel ("ESPACIO: Tirar dados", "Click derecho: Cancelar").
- Separadores visuales entre secciones del panel para mejor legibilidad.
- Sombra en el panel para efecto de profundidad visual.
- Método `draw_board()` en UI renderizando tablero completo con fichas.
- Método `draw_panel()` en UI con diseño visual mejorado y jerarquía clara.
- Método `draw_bar_fichas()` en UI para mostrar fichas capturadas.
- Método `roll_dice()` en UI manejando tirada de dados y gestión de dobles.
- Atributo `remaining_dice` en UI para controlar dados disponibles en el turno.
- Método `handle_click(pos, button)` en UI para procesar clicks del usuario.
- Método `get_clicked_point(pos)` en UI para mapear coordenadas a índices de puntos.
- Método `cancel_selection()` en UI para permitir cancelar selección con click derecho.
- Lógica de selección de fichas con resaltado dorado (15px, 3px grosor).
- Validación de movimientos por dirección: blanco antihorario (0→23), negro horario (23→0).
- Gestión automática de cambio de turno al agotar dados disponibles.
- Integración completa entre UI y lógica de `core/` sin duplicar reglas.
- Flujo de juego: tirar dados → seleccionar origen → elegir destino → validar → ejecutar.
- Manejo de reingresar desde bar con prioridad automática.
- Tests de integración verificando flujo completo de juego.
- Archivo `prompts-desarrollo.md` con prompts utilizados para corrección de direcciones y mejora de UI.

### Changed
- `Board`: estructura de puntos migrada de enteros a diccionarios `{"count", "color"}`.
- API de `Board`: getters actualizados para devolver diccionarios en vez de enteros.
- Tests de `Board`: adaptados a nueva estructura de diccionarios.
- `distance_in_direction()`: fórmulas corregidas para direcciones correctas por color.
- Validaciones de movimiento en `move_checker()`: invertidas para soportar direcciones correctas.
- Bear off: condiciones ajustadas (blanco >23, negro <0).
- Nomenclatura de atributos del bar: `self.bar_blanco` → `self.__bar_blanco__` para cumplir requisitos.
- Nomenclatura de atributos del bar: `self.bar_negro` → `self.__bar_negro__` para cumplir requisitos.
- `BackgammonUI.draw_panel()`: dimensiones aumentadas de 300x270 a 330x500 píxeles.
- `BackgammonUI.draw_panel()`: tipografías aumentadas para mejor legibilidad (18-28pt).
- `BackgammonUI.draw_panel()`: dados visuales aumentados de 35x35 a 40x40 píxeles.
- `BackgammonUI.draw_panel()`: espaciado entre secciones aumentado de 40px a 50px.
- `BackgammonUI.draw_panel()`: capacidad de mensajes aumentada de 3 a 4 líneas.
- Ajustes en reportes automáticos de cobertura y pylint.
- `JUSTIFICACION.md`: ampliado con secciones de direcciones, UI, SOLID, diagramas y evolución.

### Fixed
- Direcciones de movimiento: blancas ahora se mueven antihorario (0→23) correctamente.
- Direcciones de movimiento: negras ahora se mueven horario (23→0) correctamente.
- `distance_in_direction()`: cálculo corregido para cada color.
- Validaciones en `move_checker()`: ahora rechazan direcciones incorrectas apropiadamente.
- Bear off: condiciones corregidas para cada color.
- Acceso a atributos privados del bar en UI: uso de name mangling correcto (`_Board__bar_blanco__`).
- Arreglos en reportes generados por GitHub Actions.
- Limpieza de archivos de reportes innecesarios del repositorio.
- Bug en mapeo visual de puntos: fila superior ahora se dibuja correctamente de derecha a izquierda.
- Legibilidad del panel: tamaños de fuente aumentados y espaciado mejorado.

### Deprecated
- (Ninguno en esta versión)

### Removed
- (Ninguno en esta versión)

### Security
- (No aplica en esta versión)

## Notas de versión

### Versión actual (Sprint 3)
Esta versión incluye la primera implementación funcional de la interfaz gráfica con Pygame. Los jugadores pueden:
- Ver el tablero completo con fichas en posiciones iniciales.
- Tirar dados presionando ESPACIO.
- Seleccionar y mover fichas haciendo click.
- Capturar fichas enemigas automáticamente.
- Reingresar fichas desde el bar.
- Ver el turno actual y dados disponibles en panel lateral.

**Limitaciones conocidas:**
- Bear off no completamente implementado.
- No se detecta condición de victoria.
- CLI aún no funcional (pendiente para próximo sprint).
- Sin persistencia en Redis.

**Cobertura de tests:** [Indicar porcentaje actual]

**CodeClimate Grade:** [Indicar grado actual]

---

## Historial de Sprints

### Sprint 1 (Semanas 1-2)
**Objetivo:** Establecer estructura base y lógica fundamental.

**Completado:**
- Configuración de proyecto (estructura de carpetas, Git, CI/CD).
- Clases `Dice`, `Player`, `Checker` completamente implementadas.
- Tests unitarios con alta cobertura.
- Documentación inicial (README, CHANGELOG, JUSTIFICACION).

**Commits:** 10+ distribuidos en el período.

### Sprint 2 (Semanas 3-4)
**Objetivo:** Implementar lógica del tablero y orquestador del juego.

**Completado:**
- Clase `Board` con todas las operaciones básicas.
- Clase `BackgammonGame` como coordinador.
- Lógica de movimiento, captura y bar.
- Tests de integración entre componentes.
- Ampliación de documentación técnica.

**Commits:** 10+ distribuidos en el período.

### Sprint 3 (Semanas 5-6) - ACTUAL
**Objetivo:** Interfaz gráfica funcional con Pygame.

**Completado:**
- Clase `BackgammonUI` con renderizado completo.
- Corrección de direcciones de movimiento (blanco antihorario, negro horario).
- Panel de información mejorado visualmente.
- Flujo completo de juego: tirar dados, seleccionar, mover, capturar.
- Gestión de bar y reingresar fichas.
- Archivo de prompts según requisitos del proyecto.

**En progreso:**
- Bear off completo.
- Detección de victoria.

**Commits:** 10+ distribuidos en el período.

### Sprint 4 (Planificado: Semanas 7-8)
**Objetivo:** CLI funcional y refinamiento de reglas.

**Planeado:**
- Interfaz CLI completamente funcional.
- Bear off con todas las validaciones.
- Detección de victoria y fin de juego.
- Refactoring de código duplicado.
- Mejora de cobertura de tests a 90%+.

### Sprint 5 (Planificado: Semanas 9-10)
**Objetivo:** Características opcionales y pulido final.

**Planeado:**
- Persistencia con Redis (opcional).
- Modo vs IA (opcional).
- Animaciones y efectos visuales.
- Documentación completa para entrega.
- Preparación de defensa oral.

---

## Métricas del Proyecto

### Cobertura de Tests
- **Sprint 1:** 85%
- **Sprint 2:** 88%
- **Sprint 3:** [Actualizar]
- **Objetivo final:** 90%+

### CodeClimate
- **Mantenibilidad:** [Actualizar]
- **Issues:** 0 (objetivo cumplido)
- **Code Smells:** [Actualizar]
- **Deuda técnica:** [Actualizar]

### Líneas de Código
- **core/:** ~500 líneas
- **pygame_ui/:** ~350 líneas
- **tests/:** ~600 líneas
- **Total:** ~1450 líneas (aproximado)

### Commits
- **Total acumulado:** 30+ commits
- **Distribución:** Regular a lo largo de los sprints
- **Autores:** [Nombre del alumno]

---

## Links de Referencia

- **Repositorio:** [URL del repositorio GitHub]
- **CI/CD:** GitHub Actions + SonarCloud
- **Documentación técnica:** Ver `JUSTIFICACION.md`
- **Prompts de IA:** Ver `prompts-desarrollo.md`
- **Reglas del juego:** https://www.ludoteka.com/clasika/backgammon-es.html