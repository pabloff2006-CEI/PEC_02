
"""
Módulo encargado de gestionar las operaciones de las tareas.
"""

from typing import List, Any

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
        """Devuelve una copia de todas las tareas registradas."""

        return self._tareas.copy()

    def buscar_tarea(self, palabra: str) -> List[Tarea]:
        """Busca tareas cuyo nombre contenga la palabra indicada."""

        palabra = palabra.strip().lower()

        return [
            tarea for tarea in self._tareas
            if palabra in tarea.nombre.lower()
        ]
