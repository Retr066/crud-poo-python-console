class TaskError(Exception):
    """Clase base para excepciones en este módulo."""
    pass

class TaskNotFoundError(TaskError):
    """Excepción lanzada cuando una tarea no se encuentra."""
    def __init__(self, task_id):
        self.task_id = task_id
        self.message = f"Tarea con ID {task_id} no encontrada."
        super().__init__(self.message)

class TaskInvalidInputError(TaskError):
    """Excepción lanzada cuando la entrada del usuario es inválida."""
    def __init__(self, input_value):
        self.input_value = input_value
        self.message = f"Entrada inválida: {input_value}"
        super().__init__(self.message)

class TaskOperationError(TaskError):
    """Excepción lanzada cuando ocurre un error en una operación con tareas."""
    def __init__(self, operation, message="Error en la operación de la tarea"):
        self.operation = operation
        self.message = f"{message}: {operation}"
        super().__init__(self.message)
