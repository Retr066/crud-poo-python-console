from model import ModelTasks, ITask
from view import View
from utils.handler_error import TaskError, TaskNotFoundError


class TaskController:
    def __init__(self, model: ModelTasks, view: View) -> None:
        self.__view = view
        self.__model = model
        # print(self.__model.attributes)
        # self.__view.initialization_fields(self.__model.attributes)

    def handle_display_all_tasks(self):
        try:
            tasks = self.__model.read_tasks()
            self.__view.display_all_tasks(tasks)
        except TaskError as e:
            self.__view.handle_error(e)

    def handle_display_task(self):
        try:
            id_task = self.__view.get_task_id()
            task = self.__model.get_task(id_task)
            self.__view.display_task(task)
        except TaskError as e:
            self.__view.handle_error(e)

    def handle_create_task(self):
        try:
            name,description = self.__view.get_new_task()
            self.__model.create_task(name,description)
            self.__view.show_message('Tarea creada correctamente')
        except TaskError as e:
            self.__view.handle_error(e)

    def handle_delete_task(self):
        try:
            id_task = self.__view.get_task_id()
            self.__model.delete_task(id_task)
            self.__view.show_message('Tarea eliminada correctamente')
        except TaskError as e:
            self.__view.handle_error(e)

    def handle_update_task(self):
        try:
            id_task = self.__view.get_task_id()
            task = self.__model.get_task(id_task)
            new_task: ITask = dict()
            new_task['id'] = task.id
            if not task:
                raise TaskNotFoundError(id_task)

            new_name = self.__view.get_task_update_name(task.name)
            
            if not new_name:
                new_task["name"] = task.name
            else:
                new_task['name'] = new_name
            
            print(new_name,'name')

            new_description = self.__view.get_task_update_description(task.description)
            if not new_description:
                new_task["description"] = task.description
            else:
                new_task["description"] = new_description

            print(new_description,'description')
            new_done = self.__view.get_task_update_done(task.done)
            if new_done is None:
                new_task["done"] = task.done
            else:
                new_task['done'] = new_done

    
            self.__model.update_task(new_task)
            self.__view.show_message('Tarea actualizada correctamente')
        except TaskError as e:
            self.__view.handle_error(e)
