from db_connection import DbConnection
from managers import UserManager, CarManager, AddressManager

db = DbConnection()

if __name__ == "__main__":
    db.setup_database()

    users = UserManager(db.engine)
    cars = CarManager(db.engine)
    addresses = AddressManager(db.engine)

    user_id = users.create("oscar3-94@hotmail.com", "8888-8888")
    print(f"Usuario creado: id={user_id}")

    addresses.create(user_id, "Puriscal", "San José", "10401")

    car_id = cars.create("Susuki", "Alto", 2024)
    print(f"Auto creado: id={car_id}")

    assigned = cars.assign_to_user(car_id, user_id)
    print(f"Auto asignado a usuario: {assigned}")

    print("Usuarios:", users.get_all())
    print("Autos:", cars.get_all())
    print("Direcciones:", addresses.get_all())