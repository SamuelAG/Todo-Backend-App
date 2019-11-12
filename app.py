from flask import Flask, request, jsonify
from models import Schema
from service import TodoService

app = Flask(__name__)

@app.route("/todo", methods=["POST"])
def create_todo():
    try:
        json = request.get_json()
        print("Json: ", json)
        return jsonify(TodoService().create(json))
    except:
        return {'error' : 'invalid'}

@app.route("/delete", methods=["POST"])
def delete_todo():
    try:
        json = request.get_json()
        print("Json: ", json)
        id = json['Id']
        return jsonify(TodoService().delete(id))
    except:
        return {'error' : 'invalid'}

@app.route("/todos", methods=["GET"])                   
def getTodos():     
    return jsonify(TodoService().getTodos())

@app.route("/")                   
def hello():     
    return "Hello World!"


if __name__ == "__main__":
    Schema()
    app.run(debug=True)
