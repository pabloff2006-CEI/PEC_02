
"""
Módulo encargado de mostrar el menú y solicitar datos.
"""

from typing import Tuple

from app.imprimir_msj import MostrarMensaje


def mostrar_menu(mensajes: MostrarMensaje) -> int:
    """Muestra el menú y solicita una opción válida."""

    opciones: Tuple[str, ...] = (
        "1. Añadir tarea",
        "2. Listar tareas",
        "3. Buscar tarea",
        "4. Salir"
    )

    mensajes.mostrar_titulo("GESTOR DE TAREAS")

    for opcion in opciones:
        mensajes.imprimir_mensaje(opcion)

    seleccion = 0

    while not 1 <= seleccion <= 4:
        try:
            seleccion = int(input("\nSelecciona una opción: "))

            if not 1 <= seleccion <= 4:
                mensajes.mostrar_error("Selecciona una opción entre 1 y 4.")

        except ValueError:
            mensajes.mostrar_error("Debes introducir un número.")

    return seleccion


def solicitar_texto(
    mensajes: MostrarMensaje,
    mensaje: str,
    obligatorio: bool = True
) -> str:
    """Solicita texto y comprueba si es obligatorio."""

    valor = ""

    while obligatorio and not valor:
        valor = input(mensaje).strip()

        if not valor:
            mensajes.mostrar_error("Este campo es obligatorio.")

    if not obligatorio:
        valor = input(mensaje).strip()

    return valor


def solicitar_prioridad(mensajes: MostrarMensaje) -> str:
    """Solicita una prioridad entre Baja, Media y Alta."""

    prioridades = {
        "1": "Baja",
        "2": "Media",
        "3": "Alta"
    }

    seleccion = ""

    while seleccion not in prioridades:
        mensajes.imprimir_mensaje(
            "1. Baja\n"
            "2. Media\n"
            "3. Alta"
        )

        seleccion = input("Selecciona la prioridad: ").strip()

        if seleccion not in prioridades:
            mensajes.mostrar_error("Selecciona una prioridad válida.")

    return prioridades[seleccion]
