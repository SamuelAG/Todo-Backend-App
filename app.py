from flask import Flask, request, jsonify
from models import Schema
from service import TodoService

app = Flask(__name__)

@app.route("/todo", methods=["POST"])
def create_todo():
    json = request.get_json()
    print("Json enviado: ", json)
    return jsonify(TodoService().create(json))

if __name__ == "__main__":
    Schema()
    app.run(debug=True)