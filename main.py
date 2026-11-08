
"""
Punto de entrada del gestor de tareas.
"""

from app.operaciones import GestorTareas
from app.imprimir_msj import MostrarMensaje
from app.menu import mostrar_menu, solicitar_texto, solicitar_prioridad


def main() -> None:
    """Inicializa y ejecuta la aplicación."""

    mensajes = MostrarMensaje()
    gestor = GestorTareas()

    salir = False

    while not salir:
        try:
            opcion = mostrar_menu(mensajes)

            if opcion == 1:
                mensajes.mostrar_titulo("AÑADIR TAREA")

                nombre = solicitar_texto(mensajes, "Nombre de la tarea: ")
                prioridad = solicitar_prioridad(mensajes)

                fecha = solicitar_texto(
                    mensajes, "Fecha límite (opcional): ", False
                )

                etiqueta = solicitar_texto(
                    mensajes, "Etiqueta (opcional): ", False
                )

                tarea = gestor.añadir_tarea(
                    nombre,
                    prioridad=prioridad,
                    fecha_limite=fecha,
                    etiqueta=etiqueta
                )

                mensajes.mostrar_exito(
                    f"Tarea añadida correctamente. ID: {tarea.id}"
                )

            elif opcion == 2:
                mensajes.mostrar_titulo("LISTADO DE TAREAS")

                tareas = gestor.listar_tareas()

                if not tareas:
                    mensajes.mostrar_advertencia(
                        "No hay tareas registradas."
                    )
                else:
                    for tarea in tareas:
                        mensajes.imprimir_mensaje(str(tarea))

            elif opcion == 3:
                mensajes.mostrar_titulo("BUSCAR TAREA")

                palabra = solicitar_texto(
                    mensajes, "Introduce el nombre o palabra clave: "
                )

                resultados = gestor.buscar_tarea(palabra)

                if not resultados:
                    mensajes.mostrar_advertencia(
                        "No se encontraron tareas."
                    )
                else:
                    for tarea in resultados:
                        mensajes.imprimir_mensaje(str(tarea))

            elif opcion == 4:
                salir = True

            if not salir:
                input("\nPulsa INTRO para continuar...")

        except (ValueError, TypeError, KeyError) as error:
            mensajes.mostrar_error(str(error))

        except (KeyboardInterrupt, EOFError):
            mensajes.mostrar_advertencia("Cerrando aplicación...")
            salir = True

    mensajes.mostrar_informacion(
        "Gracias por utilizar el gestor de tareas."
    )


if __name__ == "__main__":
    main()
