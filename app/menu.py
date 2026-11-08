
"""
Módulo encargado de mostrar el menú y solicitar datos.
"""

from typing import Tuple

from colorama import Fore, Style
from app.imprimir_msj import MostrarMensaje


def mostrar_menu(mensajes: MostrarMensaje) -> int:
    """Muestra el menú y solicita una opción válida."""



    opciones: Tuple[str, ...] = (
        "Añadir tarea",
        "Listar tareas",
        "Buscar tarea",
        "Salir"
    )

    #mensajes.imprimir_mensaje(titulo)
    mensajes.mostrar_titulo("MENÚ PRINCIPAL")

    for numero, opcion in enumerate(opciones, start=1):
        mensajes.imprimir_mensaje(
            f"{Fore.LIGHTGREEN_EX}{numero}{Style.RESET_ALL}. {opcion}"
        )

    seleccion = 0

    while not 1 <= seleccion <= 4:
        try:
            seleccion = int(input("\nSelecciona una opción: "))

            if not 1 <= seleccion <= 4:
                mensajes.mostrar_error(
                    "Selecciona una opción entre 1 y 4."
                )

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
            f"{Fore.LIGHTGREEN_EX}1{Style.RESET_ALL}. Baja\n"
            f"{Fore.LIGHTGREEN_EX}2{Style.RESET_ALL}. Media\n"
            f"{Fore.LIGHTGREEN_EX}3{Style.RESET_ALL}. Alta"
        )

        seleccion = input("Selecciona la prioridad: ").strip()

        if seleccion not in prioridades:
            mensajes.mostrar_error("Selecciona una prioridad válida.")

    return prioridades[seleccion]
