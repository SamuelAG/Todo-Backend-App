from models import TodoModel

class TodoService:
    def __init__(self):
        self.model = TodoModel()

    def create(self, params):
        self.model.create(params)
    
    def delete(self, params):
        self.model.delete(params)

    def update(self, params):
        self.model.updateTodo(params)

    def getTodos(self):
        return self.model.getTodos()