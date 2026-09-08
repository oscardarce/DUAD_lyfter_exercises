from db_connection import DbConnection
from managers import UserManager, CarManager, AddressManager, UserNotFoundError

if __name__ == "__main__":
    db = DbConnection()
    db.setup_database()

    users = UserManager(db.Session)
    cars = CarManager(db.Session)
    addresses = AddressManager(db.Session)

    # CREATE
    user_id = users.create("oscar3-94@hotmail.com", "8888-8888")
    print(f"Usuario creado: id={user_id}")

    address_id = addresses.create(user_id, "Puriscal", "San José", "10401")
    print(f"Dirección creada: id={address_id}")

    car_id = cars.create("Susuki", "Alto", 2024)
    print(f"Auto creado (sin dueño): id={car_id}")

    assigned = cars.assign_to_user(car_id, user_id)
    print(f"Auto asignado a usuario: {assigned}")

    # UPDATE
    users.update(user_id, phone_number="8888-9999")

    addresses.update(address_id, city="Acosta")

    cars.update(car_id, year=2025)

    # Si el user id es inexistente se rechaza antes de tocar la DB
    try:
        cars.create("Toyota", "Yaris", 2023, user_id=99999)
    except UserNotFoundError as e:
        print(f"Error al crear auto: {e}")

    try:
        addresses.create(99999, "Calle Falsa", "Ciudad", "00000")
    except UserNotFoundError as e:
        print(f"Error al crear dirección: {e}")

    # --- DELETE ---
    deleted_address = addresses.delete(address_id)
    print(f"Dirección eliminada: {deleted_address}")

    deleted_car = cars.delete(car_id)
    print(f"Auto eliminado: {deleted_car}")

    deleted_user = users.delete(user_id)
    print(f"Usuario eliminado: {deleted_user}")
