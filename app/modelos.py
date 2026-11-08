
"""
Módulo encargado de definir el modelo de las tareas.
"""

from typing import Dict, Any


class Tarea:
    """Representa una tarea del gestor."""

    def __init__(
        self,
        id_tarea: int,
        nombre: str,
        **kwargs: Any
    ):
        """Inicializa una tarea con sus datos y metadatos opcionales."""

        self.id = id_tarea
        self.nombre = nombre
        self.metadatos: Dict[str, Any] = kwargs

    def __str__(self) -> str:
        """Devuelve la información de la tarea."""

        return f"ID: {self.id} | Nombre: {self.nombre} | Datos: {self.metadatos}"
