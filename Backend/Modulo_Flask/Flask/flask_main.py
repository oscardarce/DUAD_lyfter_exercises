from flask import Flask, jsonify, request
import json
import os


# Este es el punto de entrada a la aplicación
app = Flask(__name__)

# Este es el path relativo de donde nos encontremos ubicados en los archivos de nuestro sistema operativo
TASK_LIST_PATH = os.path.join(os.path.dirname(__file__), "tasks_data.json")

# Arreglo necesario para inicializar JSON vacio en caso de que no exista un JSON
task_list = []

# Unicos estados
valid_states = ["Por Hacer", "En Progreso", "Completada"]


def load_or_create_json():
    # Modificamos la variable que está declarada fuera, para no crear una nueva variable local.
    global task_list

    if os.path.exists(TASK_LIST_PATH):
        with open(TASK_LIST_PATH, "r", encoding="utf-8") as file:
            task_list = json.load(file)
    else:
        task_list = []
        with open(TASK_LIST_PATH, "w", encoding="utf-8") as file:
            json.dump(task_list, file, indent=2)


# Mostrar en POSTMAN mensaje de solicitud al API y el total de tareas en la base de datos.
@app.route("/", methods=["GET"])
def main():
    return jsonify({
        "mensaje": "API de tareas activa",
        "total_tareas": len(task_list),
    })


# Crear data
@app.route("/create", methods=["POST"])
def create():

    try:
        # Validaciones
        if "id" not in request.json:
            raise ValueError("La request debe tener un id")
        if "title" not in request.json:
            raise ValueError("La request debe tener un titulo")
        if "description" not in request.json:
            raise ValueError("La request debe tener una descripción")
        if "state" not in request.json:
            raise ValueError("La request debe tener un estado")
        if request.json["state"] not in valid_states:
            raise ValueError(
                "El estado debe ser: Por Hacer, En Progreso o Completada")
        if any(task["id"] == request.json["id"] for task in task_list):
            raise ValueError("El id ya existe")

        # Request
        nueva_tarea = {
            "id":          request.json["id"],
            "title":       request.json["title"],
            "description": request.json["description"],
            "state":       request.json["state"],
        }
        # Guardar la data en memoria
        task_list.append(nueva_tarea)

        # Guardamos la data en la base de datos
        with open(TASK_LIST_PATH, "w", encoding="utf-8") as file:
            json.dump(task_list, file, indent=2)

        return jsonify({"mensaje": "Tarea creada", "tarea": nueva_tarea}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# Listar data
@app.route("/list", methods=["GET"])
def get():
    state_filter = request.args.get("state")

    # Devolvemos solo lo que venga en los querys parameters que contenga el mismo estado
    if state_filter:
        filtered_tasks = [
            task for task in task_list if task["state"] == state_filter]
        return jsonify({
            "total": len(filtered_tasks),
            "tareas": filtered_tasks
        }), 200
    else:
        return jsonify({
            "total": len(task_list),
            "tareas": task_list
        }), 200


# Editar data
@app.route("/edit", methods=["PUT"])
def edit():
    try:
        task_id = request.json.get("id")
        task_title = request.json.get("title")

        if not task_id and not task_title:
            raise ValueError(
                "Debes enviar el id o el titulo de la tarea a editar")

        task_found = None

        # Validamos editar por ID o por Titulo
        for task in task_list:
            if task["id"] == task_id:
                task_found = task
                break
            if task["title"] == task_title:
                task_found = task
                break

        if not task_found:
            raise ValueError(f"No existe una tarea con id {task_id}")

        # Puede venir el id en el request pero si el id es diferente del id en principio da error (no se puede cambiar)
        if "id" in request.json and request.json["id"] != task_found["id"]:
            raise ValueError("El id de la tarea no se puede modificar")

        if "title" in request.json:
            task_found["title"] = request.json["title"]
        if "description" in request.json:
            task_found["description"] = request.json["description"]
        if "state" in request.json:
            task_found["state"] = request.json["state"]

        with open(TASK_LIST_PATH, "w", encoding="utf-8") as file:
            json.dump(task_list, file, indent=2)

        return jsonify({"mensaje": "Tarea actualizada", "tarea": task_found}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# Eliminar ada
@app.route("/delete", methods=["DELETE"])
def delete():
    try:
        task_id = request.json.get("id")

        if not task_id:
            raise ValueError(
                "Debes enviar el id para poder eliminar una tarea")

        task_found = None

        for task in task_list:
            if task["id"] == task_id:
                task_found = task
                break

        if not task_found:
            raise ValueError(f"No existe una tarea con id {task_id}")

        task_list.remove(task_found)
        with open(TASK_LIST_PATH, "w", encoding="utf-8") as file:
            json.dump(task_list, file, indent=2)

        return jsonify({"mensaje": "Tarea eliminada", "tarea": task_found}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    # Cargamos datos de un Json ya creado o se crea limpio []
    load_or_create_json()
    app.run(host="localhost", debug=True)
