from sqlalchemy import select
from models import User, Car, Address


class UserNotFoundError(Exception):
    """Se lanza cuando se referencia un user_id que no existe en la base de datos."""


def validate_user_exists(session, user_id):

    if user_id is not None and session.get(User, user_id) is None:
        raise UserNotFoundError(f"No existe un usuario con id={user_id}")


class BaseManager:
    model = None  # cada subclase la define

    def __init__(self, session_factory):
        self.session_factory = session_factory

    def update(self, row_id, **fields):
        if not fields:
            return False
        with self.session_factory() as session:
            obj = session.get(self.model, row_id)
            if obj is None:
                return False
            for key, value in fields.items():
                setattr(obj, key, value)
            session.commit()
            return True

    def delete(self, row_id):
        with self.session_factory() as session:
            obj = session.get(self.model, row_id)
            if obj is None:
                return False
            session.delete(obj)
            session.commit()
            return True

    def get_all(self):
        with self.session_factory() as session:
            return session.scalars(select(self.model)).all()


class UserManager(BaseManager):
    model = User

    def create(self, email_address, phone_number=None):
        with self.session_factory() as session:
            user = User(email_address=email_address, phone_number=phone_number)
            session.add(user)
            session.commit()
            return user.id


class CarManager(BaseManager):
    model = Car

    def create(self, brand, model, year, user_id=None):
        with self.session_factory() as session:
            validate_user_exists(session, user_id)
            car = Car(brand=brand, model=model, year=year, user_id=user_id)
            session.add(car)
            session.commit()
            return car.id

    def assign_to_user(self, car_id, user_id):
        with self.session_factory() as session:
            validate_user_exists(session, user_id)
            car = session.get(Car, car_id)
            if car is None:
                return False
            car.user_id = user_id
            session.commit()
            return True


class AddressManager(BaseManager):
    model = Address

    def create(self, user_id, street, city, zip_code):
        with self.session_factory() as session:
            validate_user_exists(session, user_id)
            address = Address(user_id=user_id, street=street,
                              city=city, zip_code=zip_code)
            session.add(address)
            session.commit()
            return address.id
