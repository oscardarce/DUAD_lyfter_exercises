from flask import Flask, request, jsonify
from db_manager import UserRepository, CarRepository, RentalRepository
from db_connection import ConnectionManager

app = Flask(__name__)

# Inicialización de la conexión y repositorios
db_connection = ConnectionManager()
user_repo = UserRepository(db_connection)
car_repo = CarRepository(db_connection)
rental_repo = RentalRepository(db_connection)


# Post
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json

    required_fields = ["first_name", "email",
                       "username", "password", "birthdate"]
    if not data or any(not data.get(field) for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    user_id = user_repo.add_user(
        data.get("first_name"), data.get("email"),
        data.get("username"), data.get("password"),
        data.get("birthdate")
    )
    if user_id:
        return jsonify({"message": "User created", "id": user_id}), 201
    return jsonify({"error": "Could not create user"}), 500


@app.route("/cars", methods=["POST"])
def create_car():
    data = request.json

    required_fields = ["brand", "model", "year"]
    if not data or any(not data.get(field) for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    car_id = car_repo.add_car(
        data.get("brand"), data.get("model"), data.get("year"))
    if car_id:
        return jsonify({"message": "Car created", "id": car_id}), 201
    return jsonify({"error": "Could not create car"}), 500


@app.route("/rentals", methods=["POST"])
def create_rental():
    data = request.json

    if not data or not data.get("user_id") or not data.get("car_id"):
        return jsonify({"error": "Missing user_id or car_id"}), 400

    rental_id = rental_repo.create_rental(
        data.get("user_id"), data.get("car_id"))
    if rental_id:
        return jsonify({"message": "Rental created successfully", "id": rental_id}), 201
    return jsonify({"error": "Could not create rental (car unavailable or does not exist)"}), 400


# Put
@app.route("/cars/<int:car_id>/state", methods=["PUT"])
def change_car_state(car_id):
    new_state = request.json.get("state")
    if not new_state:
        return jsonify({"error": "Missing state"}), 400

    if car_repo.update_car_state(car_id, new_state):
        return jsonify({"message": f"Car state updated to {new_state}"})
    return jsonify({"error": "Error updating car state"}), 400


@app.route("/users/<int:user_id>/state", methods=["PUT"])
def change_user_state(user_id):
    new_state = request.json.get("state")
    if not new_state:
        return jsonify({"error": "Missing state"}), 400

    if user_repo.update_user_state(user_id, new_state):
        return jsonify({"message": f"User state updated to {new_state}"})
    return jsonify({"error": "Error updating user state"}), 400


@app.route("/users/<int:user_id>/flag", methods=["PUT"])
def flag_user_defaulted(user_id):
    if user_repo.update_user_state(user_id, "defaulted"):
        return jsonify({"message": "User flagged as defaulted"})
    return jsonify({"error": "Error flagging user"}), 400


@app.route("/rentals/<int:rental_id>/state", methods=["PUT"])
def change_rental_state(rental_id):
    new_state = request.json.get("state")
    if not new_state:
        return jsonify({"error": "Missing state"}), 400

    if rental_repo.update_rental_state(rental_id, new_state):
        return jsonify({"message": f"Rental state updated to {new_state}"})
    return jsonify({"error": "Error updating rental state"}), 400


@app.route("/rentals/<int:rental_id>/complete", methods=["PUT"])
def complete_rental(rental_id):
    if rental_repo.complete_rental(rental_id):
        return jsonify({"message": "Rental completed and car marked as available"})
    return jsonify({"error": "Error completing rental or already completed"}), 400


# Get
@app.route("/users", methods=["GET"])
def list_users():
    filters = request.args.to_dict()
    users = user_repo.get_filtered_data("users", filters)
    return jsonify(users)


@app.route("/cars", methods=["GET"])
def list_cars():
    filters = request.args.to_dict()
    cars = car_repo.get_filtered_data("cars", filters)
    return jsonify(cars)


@app.route("/rentals", methods=["GET"])
def list_rentals():
    filters = request.args.to_dict()
    rentals = rental_repo.get_filtered_data("car_rental", filters)
    return jsonify(rentals)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
