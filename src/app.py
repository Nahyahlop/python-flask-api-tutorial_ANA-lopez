# Importando herramientas de Flask:
from flask import Flask
from flask import jsonify
from flask import request

# Creando el Servidor
app = Flask(__name__)

# Creando mi "base de datos"
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# ENDPOINT 1 → GET /todos
@app.route('/todos', methods=['GET'])
# Nombre de la función (podría llamarse cualquier cosa)
def hello_world():
    # Convierte la lista a formato JSON
    json_text = jsonify(todos)
    # Devuelve la lista al cliente
    return json_text

# ENDPOINT 2 → POST /todos
@app.route('/todos', methods=['POST'])
# Función que maneja la creación
def add_new_todo():
    # Estás leyendo lo que el cliente envía
    request_body = request.json
    # Solo para ver en consola lo que llega (debug)
    print("Incoming request with the following body", request_body)
    # Añadimos la nueva tarea a la lista
    todos.append(request_body)
    # Devuelves la lista actualizada
    return jsonify(todos)

# ENDPOINT 3 → DELETE /todos/<position>
# <int:position> → es una variable en la URL
@app.route('/todos/<int:position>', methods=['DELETE'])
# Flask automáticamente te pasa ese número aquí
def delete_todo(position):
    # Para debug
    print("This is the position to delete:", position)
    # elimina un elemento por índice
    todos.pop(position)
    # Devuelve la lista actualizada
    return jsonify(todos)

# ARRANCAR EL SERVIDOR
# Solo ejecuta esto si estoy corriendo este archivo directamente"
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
  
# host='0.0.0.0' → accesible desde fuera
# port=3245 → en qué puerto corre
# debug=True → muestra errores automáticamente