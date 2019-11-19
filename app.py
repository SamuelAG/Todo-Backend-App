from flask import Flask, request, jsonify
from models import Schema
from service import TodoService

app = Flask(__name__)

@app.route("/todo", methods=["POST"])
def create_todo():
    try:
        json = request.get_json()
        return jsonify(TodoService().create(json))
    except:
        return {'error' : 'invalid'}

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_todo(id):
    return jsonify(TodoService().delete(id))

@app.route("/update/<int:id>", methods=["PUT"])
def update_todo(id):
    return jsonify(TodoService().update(id))

@app.route("/todos", methods=["GET"])                   
def getTodos():     
    return jsonify(TodoService().getTodos())

@app.route("/")                   
def hello():     
    return "Hello World!"


if __name__ == "__main__":
    Schema()
    app.run(debug=True)