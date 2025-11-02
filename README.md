# Trabajo Final de Computación

## Proyecto: Juego de Backgammon

**Alumna:** María Eva Modarelli  
**Carrera:** Ingeniería en Informática  
**Materia:** Computación  
**Año:** 2025

---

## Descripción general

Este proyecto consiste en la implementación completa del juego de **Backgammon** en **Python**.  
Se desarrolló una versión jugable tanto en **modo texto (CLI)** como con **interfaz gráfica (Pygame)**.

El objetivo principal es aplicar los conceptos de **programación orientada a objetos (POO)**, control de flujo, manejo de excepciones y **testing automatizado**, asegurando un diseño modular y mantenible.

---

## Estructura del proyecto

```
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
```

---

## Entorno virtual y dependencias

1. **Crear entorno virtual:**
   ```bash
   python3 -m venv nombre_del_entorno
   ```

2. **Activar entorno virtual:**
   ```bash
   source nombre_del_entorno/bin/activate     # Linux / macOS
   nombre_del_entorno\Scripts\activate        # Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

El archivo `requirements.txt` incluye las bibliotecas necesarias:

```
pygame
coverage
unittest
```

---

## Ejecución del juego

### Modo texto (CLI)
```bash
python3 cli/test_game.py
```

### Modo gráfico (Pygame)
```bash
python3 pygame_ui/game_window.py
```

---

## Testing y cobertura

Los tests se implementaron con el módulo estándar `unittest`.  
Para ejecutar todos los tests y generar el reporte de cobertura:

```bash
coverage run -m unittest discover
coverage report -m
```

Esto genera un reporte con el porcentaje de cobertura de código.  
El objetivo del proyecto es alcanzar **al menos un 90 % de cobertura** sobre el código fuente.

---

## Diseño y principios aplicados

- **Programación Orientada a Objetos (POO):** cada entidad (tablero, jugador, ficha, dado) se modeló como una clase independiente.  
- **Principios SOLID:** se aplicaron los principios de responsabilidad única, bajo acoplamiento y alta cohesión.  
- **Testing unitario:** se cubren los módulos `core` y `cli` para garantizar consistencia lógica.  
- **Visualización:** el módulo `pygame_ui` ofrece una interfaz gráfica funcional e intuitiva.

---

## Créditos

Proyecto desarrollado por **María Eva Modarelli**  
como parte del **Trabajo Final de la materia Computación – Ingeniería en Informática (UM – 2025)**.
