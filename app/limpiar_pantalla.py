
"""
Módulo encargado de limpiar la terminal.
"""

import os


def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo."""

    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)
