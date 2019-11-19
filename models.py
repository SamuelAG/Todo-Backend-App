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
          _is_done boolean DEFAULT 0,
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
    
    def delete(self, id):
        query = "delete from Todo where id = "
        query += str(id)
        result = self.conn.execute(query)
        return result

    def updateTodo(self, id):
        getId = "select _is_done from Todo where id = "
        getId += str(id)
        isDone = self.conn.execute(getId).fetchall()[0][0]
        query = "update Todo set _is_done = {} where id = {}"
        if isDone == 1: isDone = 0 
        else: isDone = 1 
        query = query.format(isDone, id)
        #   print(query)
        self.conn.execute(query)

    def getTodos(self):
        query = "select * from Todo"
        result_set = self.conn.execute(query).fetchall()
        keys = {
            "Id": 1,
            "Title" : "title",
            "Description" : "description",
            "_is_done" : False,
            "CreatedOn" : "data",
            "DueDate" : "date",
        }.keys()

        result = [{column: row[i]
                  for i, column in enumerate(keys)}
                  for row in result_set]
        #print(result)
        return result      