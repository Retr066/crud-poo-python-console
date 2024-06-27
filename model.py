from typing import List, Optional
from abc import ABC, abstractmethod
from utils.handler_error import TaskNotFoundError, TaskOperationError


class ITask(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @name.setter
    @abstractmethod
    def name(self, name: str) -> None:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @description.setter
    @abstractmethod
    def description(self, description: str) -> None:
        pass

    @property
    @abstractmethod
    def done(self) -> bool:
        pass

    @done.setter
    @abstractmethod
    def done(self, done: bool) -> None:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


class Task(ITask):
    def __init__(
        self, id_task: int, name: str, description: str, done: bool = False
    ) -> None:
        self.__id: int = id_task
        self.__name = name
        self.__description = description
        self.__done = done

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description

    @property
    def done(self) -> bool:
        return self.__done

    @done.setter
    def done(self, done: bool) -> None:
        self.__done = done

    def __repr__(self) -> str:
        return f"Task(id={self.id}, name={self.name}, description={self.description}, done={self.done})"


class ModelTasks:
    def __init__(self) -> None:
        self.__tasks: List[ITask] = list()

    def create_task(self, name: str, description: str):
        current_id = self.current_id()
        task = Task(current_id,name, description)
        self.__tasks.append(task)


    def current_id(self):
        if self.__tasks:
            # Devolver el ID del último elemento + 1
            return self.__tasks[-1].id + 1
        else:
            # Si la lista está vacía, devolver 1
            return 1

    def read_tasks(self):
        if not self.__tasks:
            raise TaskOperationError("opción 1", "No hay tareas")
        
        return self.__tasks

    def get_task(self, task_id) -> Optional[Task]:
        for task in self.__tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundError(task_id)

    def delete_task(self, task_id) -> None:
        task_to_remove = None
        for task in self.__tasks:
            if task.id == task_id:
                task_to_remove = task

        if task_to_remove:
            self.__tasks.remove(task_to_remove)
        else:
            raise TaskNotFoundError(task_id)

    def update_task(self, new_task):
        obj_task = Task(new_task['id'],new_task['name'],new_task['description'],new_task['done'])
        for i, task in enumerate(self.__tasks):
            if task.id == obj_task.id:
                self.__tasks[i] = obj_task
                return
        raise TaskNotFoundError(new_task['id'])

