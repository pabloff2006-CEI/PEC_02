
"""
Módulo encargado de gestionar las operaciones de las tareas.
"""

from typing import List, Any

from colorama import Fore, Style
from app.modelos import Tarea


class GestorTareas:
    """Gestiona las tareas registradas."""

    def __init__(self):
        """Inicializa la colección de tareas."""

        self._tareas: List[Tarea] = []
        self._siguiente_id = 1

    def añadir_tarea(self, nombre: str, **kwargs: Any) -> Tarea:
        """Crea y registra una tarea con metadatos opcionales."""

        tarea = Tarea(self._siguiente_id, nombre, **kwargs)

        self._tareas.append(tarea)
        self._siguiente_id += 1

        return tarea

    def listar_tareas(self) -> List[Tarea]:
        """Devuelve todas las tareas registradas."""

        return self._tareas.copy()

    def buscar_tarea(self, palabra: str) -> List[Tarea]:
        """Busca tareas cuyo nombre contenga la palabra indicada."""

        palabra = palabra.strip().lower()

        return [
            tarea for tarea in self._tareas
            if palabra in tarea.nombre.lower()
        ]

    def formatear_tarea(self, tarea: Tarea) -> str:
        """Devuelve una representación visual y coloreada de una tarea."""

        separador = Fore.MAGENTA + "=" * 45 + Style.RESET_ALL

        prioridad = tarea.metadatos.get("prioridad", "Media")
        fecha = tarea.metadatos.get("fecha_limite") or "Sin especificar"
        etiqueta = tarea.metadatos.get("etiqueta") or "Sin etiqueta"

        colores_prioridad = {
            "Baja": Fore.GREEN,
            "Media": Fore.YELLOW,
            "Alta": Fore.RED
        }

        color_prioridad = colores_prioridad.get(
            prioridad, Fore.WHITE
        )

        return (
            f"\n{separador}\n"
            f"{Fore.MAGENTA}{Style.BRIGHT}  TAREA Nº {tarea.id}{Style.RESET_ALL}\n"
            f"{separador}\n"
            f"{Fore.WHITE}{Style.BRIGHT}  Nombre: {tarea.nombre}{Style.RESET_ALL}\n"
            f"{Fore.CYAN}  Prioridad:    {color_prioridad}{prioridad}{Style.RESET_ALL}\n"
            f"{Fore.CYAN}  Fecha límite: {fecha}{Style.RESET_ALL}\n"
            f"{Fore.CYAN}  Etiqueta:     {etiqueta}{Style.RESET_ALL}\n"
            f"{separador}"
        )
