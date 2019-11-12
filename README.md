# Todo-App-Backend
Todo Backend app build with Flask

`git clone https://github.com/SamuelAG/Todo-App-Backend.git`

`cd Todo-App-Backend`

`python3 app.py`

## Make a request  


```python
import requests
requests.post("http://127.0.0.1:5000/todo", 
              json={"Title":"Titulo da todo", 
                    "Description":"Descrição da todo"
                    "DueDate Date('2019-12-01')"})
```
