from prettytable import PrettyTable
from model import ITask


class View:
    def __init__(self) -> None:
        self.__table = PrettyTable()
        self.__table.field_names = ["Id", "Nombre", "Descripción", "Completado"]

    def convert_for_prettytable(self, task: ITask):
        if not task:
            return None
        return [task.id, task.name, task.description, task.done]

    def display_all_tasks(self, tasks):
        for task in tasks:
            self.__table.add_row(self.convert_for_prettytable(task))

        print(self.__table)
        self.__table.clear_rows()

    def display_task(self, task: ITask):
        self.__table.add_row(self.convert_for_prettytable(task))
        print(self.__table)
        self.__table.clear_rows()

    def get_option_input(self):
        try:
            return int(input("Ingresar una opción: "))
        except ValueError:
            print(ValueError("Error: Debe seleccionar una opción valida"))

    def get_task_id(self):
        try:
            return int(input("Ingrese el ID de la tarea: "))
        except ValueError:
            print(ValueError("Error: El id debe ser un numero"))

    def get_task_update_name(self, current_name):
        print(f"Nombre de la tarea actual: {current_name}")
        return input("Nuevo nombre (deja en blanco para mantener la actual): ")

    def get_task_update_description(self, current_description):
        print(f"Descripción actual: {current_description}")
        return input("Nueva descripción (deja en blanco para mantener la actual): ")

    def get_task_update_done(self, current_completed):
        current_status = "Completada" if current_completed else "No completada"
        print(f"Estado actual: {current_status}")
        while True:
            completed_input = (
                input(
                    "Nueva estado (completada/no completada, deja en blanco para mantener el actual): "
                )
                .strip()
                .lower()
            )
            if completed_input == "":
                return None
            elif completed_input == "completada":
                return True
            elif completed_input == "no completada":
                return False
            else:
                print(
                    "Entrada no válida. Por favor, ingrese 'completada' o 'no completada'."
                )

    def get_new_task(self):
        name = input("Ingrese el nombre de la tarea: ")
        description = input("Ingrese la description de la tarea: ")

        return [name, description]

    def show_message(self, message):
        print(message)

    def handle_error(self, error):
        print(f"Error: {error}")
