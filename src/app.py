from flask import Flask, jsonify, request


app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

#todo_to_post = {"label":"my task number 3", "done": True}

@app.route('/todos', methods=['GET'])
def get_todos():
    list_of_todos = jsonify(todos)
    return list_of_todos

@app.route('/todos', methods=['POST'])
def post_todos():
    request_body = request.get_json(silent=True)
    if request_body is None:
        return jsonify({"msn_vacio":"No has mandado ningun mensaje"}),400
    todos.append(request_body)
    print(todos)
    #print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todos(position):
    todos.pop(position)
    print(todos)
    return 'eliminacion existosa'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)