import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_to_do_table()

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          Title TEXT,
          Description TEXT,
          _is_done boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date
        );
        """

        self.conn.execute(query)
        

class TodoModel:
    TABLENAME = "Todo"

    def __init__(self):    
        self.conn = sqlite3.connect('todo.db')

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create(self, params):
        query = f'insert into {self.TABLENAME} ' \
                f'(Title, Description, DueDate) ' \
                f'values ("{params.get("Title")}","{params.get("Description")}",' \
                f'"{params.get("DueDate")}")'
        result = self.conn.execute(query)
        return result
        