from model import ModelTasks
from view import View
from controller import TaskController
from utils.handler_error import TaskInvalidInputError,TaskError

class TaskApp:
    def __init__(self) -> None:
        self.__active: bool = True
        self.__view = View()
        self.__model = ModelTasks()
        self.__task_controller = TaskController(self.__model,self.__view)


    def run(self):
        while self.__active:
            self.message_actions()
            self.handler_actions()

    def message_actions(self):
        self.__view.show_message("Bienvenido al sistema de tareas")
        self.__view.show_message("""
            Las opciones son las siguientes
              1- Mostrar las tareas
              2- Mostrar una tarea en especifica
              3- Agregar una tarea
              4- Eliminar una tarea
              5- Actualizar una tarea
              6- Salir del programa
            """)

    def handler_actions(self):
        try:
            option = self.__view.get_option_input()
            if option == 1:
                self.__task_controller.handle_display_all_tasks()
            elif option == 2:
                self.__task_controller.handle_display_task()
            elif option == 3:
                self.__task_controller.handle_create_task()
            elif option == 4:
                self.__task_controller.handle_delete_task()
            elif option == 5:
                self.__task_controller.handle_update_task()
            elif option == 6:
                self.close()
            else:
                raise TaskInvalidInputError(option)
        except TaskError as e:
            self.__view.handle_error(e)


    def close(self):
        self.__active = False


if __name__ == "__main__":
    task_app = TaskApp()
    task_app.run()
