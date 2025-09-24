# Changelog
Todas las modificaciones notables de este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Added
- Método `is_double()` en `Dice` y sus tests (#8).
- Validación en `Player` para un máximo de 15 fichas (#15).
- Métodos `get/set_checkers` en `Player` y sus tests (#15).
- Validaciones en `set_name` y `set_color` en `Player` (#15).
- Métodos `get_name` y `set_name` en `Player` y sus tests (#15).
- Métodos `get_color` y `set_color` en `Player` y sus tests (#15).
- Clase `Board` inicializada con 24 posiciones vacías (#29).
- Método `reset_starting_position()` en `Board` y sus tests (#29).

### Changed
- Algunos tests de `Dice` actualizados para mejorar cobertura.
- Ajustes en reportes automáticos de cobertura y pylint.

### Fixed
- Arreglos en reportes generados por GitHub Actions.
- Limpieza de archivos de reportes innecesarios del repositorio.

### Added
- Clase `Dice` con `__init__`, `roll()`, getters y setters.
- Tests iniciales de `Dice`.
- Documento `JUSTIFICACION.md`.
- Documento `CHANGELOG.md` (estructura inicial).
- Estructura base del proyecto (`core/`, `cli/`, `tests/`).
- Configuración inicial de GitHub Actions + SonarCloud.
