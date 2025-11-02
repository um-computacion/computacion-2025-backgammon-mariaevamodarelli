
# Prompts de Documentación

Este archivo recopila los prompts utilizados para generar documentación del proyecto **Backgammon Computación 2025**, incluyendo el `README.md` y `JUSTIFICACION.md`.

---

##  Prompt 1 — Archivo `README.md`

**Modelo / herramienta usada:** ChatGPT (GPT-5)

**Prompt exacto:**
> Necesito que me generes el archivo `README.md` para mi proyecto Backgammon Computación 2025.  
> Debe explicar cómo ejecutar el juego en modo testing y en modo CLI, incluir dependencias, comandos Docker y breve descripción del proyecto.  
> No incluyas emojis, mantené tono formal.

**Respuesta / resultado completo:**
> ChatGPT generó un `README.md` con:
> - Descripción del juego y objetivos.  
> - Instrucciones para ejecutar en modo testing (`pytest`) y modo juego (`python cli/main.py`).  
> - Ejemplo de `docker run` para desplegar ambos modos.  
> - Créditos y referencias a documentación (Keep a Changelog, Pygame, etc.).

**Uso:**
> El archivo `README.md` final fue subido al repositorio principal.

**Referencias a archivos finales:**
> `/README.md`

---

##  Prompt 2 — Archivo `JUSTIFICACION.md`

**Modelo / herramienta usada:** ChatGPT (GPT-5)

**Prompt exacto:**
> Necesito que me generes el archivo `JUSTIFICACION.md` para mi proyecto Backgammon Computación 2025, siguiendo los requisitos del punto 4.5 del documento guía.  
> Debe incluir: resumen del diseño general, justificación de clases y atributos, decisiones de diseño, manejo de excepciones, testing, principios SOLID y un anexo UML.  
> Basate en el documento oficial del TP que te paso y en la estructura del proyecto (core, cli, pygame_ui).  
> Mantené formato Markdown y tono técnico.

**Respuesta / resultado completo:**
> ChatGPT generó un archivo `JUSTIFICACION.md` con secciones completas:  
> - Resumen del diseño general (separación de capas core/UI).  
> - Justificación de las clases `Game`, `Board`, `Player`, `Dice`, `Checker`, `CLI`, `PygameUI`.  
> - Decisiones de diseño relevantes (uso de objetos, SOLID, testing CLI, exclusión de Pygame).  
> - Diagrama UML en texto (PlantUML).  
> Se revisó y ajustó el texto para adaptarlo al código real del repositorio.

**Uso:**
> El archivo `JUSTIFICACION.md` final fue subido a la raíz del repositorio.

**Referencias a archivos finales:**
> `/JUSTIFICACION.md`
