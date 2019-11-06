from models import TodoModel

class TodoService:
    def __init__(self):
        self.model = TodoModel()

    def create(self, params):
        self.model.create(params)