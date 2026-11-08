
"""
Módulo encargado de mostrar mensajes.
"""

from colorama import init, Fore, Style


class MostrarMensaje:
    """Centraliza los mensajes de la terminal."""

    def __init__(self):
        """Inicializa Colorama."""

        init(autoreset=True)

    def imprimir_mensaje(self, msj: str):
        """Imprime un mensaje."""

        print(msj)

    def mostrar_exito(self, msj: str):
        """Muestra un mensaje de éxito."""

        self.imprimir_mensaje(f"{Fore.GREEN}{msj}{Style.RESET_ALL}")

    def mostrar_error(self, msj: str):
        """Muestra un mensaje de error."""

        self.imprimir_mensaje(f"{Fore.RED}{msj}{Style.RESET_ALL}")

    def mostrar_advertencia(self, msj: str):
        """Muestra una advertencia."""

        self.imprimir_mensaje(f"{Fore.YELLOW}{msj}{Style.RESET_ALL}")

    def mostrar_informacion(self, msj: str):
        """Muestra información."""

        self.imprimir_mensaje(f"{Fore.CYAN}{msj}{Style.RESET_ALL}")

    def mostrar_titulo(self, msj: str):
        """Muestra un título."""

        separador = "=" * 50

        self.imprimir_mensaje(
            f"\n{Fore.MAGENTA}{separador}\n"
            f"{msj.center(50)}\n"
            f"{separador}{Style.RESET_ALL}"
        )
