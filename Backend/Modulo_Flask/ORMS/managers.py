from sqlalchemy import insert, update, delete, select
from tables import users_table, cars_table, addresses_table


class BaseManager:
    table = None  # cada subclase la define

    def __init__(self, engine):
        self.engine = engine

    def update(self, row_id, **fields):
        if not fields:  # update sin valores genera SQL inválido (SET vacío)
            return False
        statement = update(self.table).where(self.table.c.id == row_id).values(**fields)
        with self.engine.begin() as conn:
            return conn.execute(statement).rowcount > 0

    def delete(self, row_id):
        statement = delete(self.table).where(self.table.c.id == row_id)
        with self.engine.begin() as conn:
            return conn.execute(statement).rowcount > 0

    def get_all(self):
        with self.engine.connect() as conn:
            return conn.execute(select(self.table)).all()


class UserManager(BaseManager):
    table = users_table

    def create(self, email_address, phone_number=None):
        statement = (
            insert(users_table)
            .values(email_address=email_address, phone_number=phone_number)
            .returning(users_table.c.id)
        )
        with self.engine.begin() as conn:
            return conn.execute(statement).scalar_one()


class CarManager(BaseManager):
    table = cars_table

    def create(self, brand, model, year, user_id=None):
        statement = (
            insert(cars_table)
            .values(brand=brand, model=model, year=year, user_id=user_id)
            .returning(cars_table.c.id)
        )
        with self.engine.begin() as conn:
            return conn.execute(statement).scalar_one()

    def assign_to_user(self, car_id, user_id):
        validate = select(users_table.c.id).where(users_table.c.id == user_id)
        statement = update(cars_table).where(cars_table.c.id == car_id).values(user_id=user_id)
        with self.engine.begin() as conn:
            if conn.execute(validate).first() is None:
                return False
            return conn.execute(statement).rowcount > 0


class AddressManager(BaseManager):
    table = addresses_table

    def create(self, user_id, street, city, zip_code):
        statement = (
            insert(addresses_table)
            .values(user_id=user_id, street=street, city=city, zip_code=zip_code)
            .returning(addresses_table.c.id)
        )
        with self.engine.begin() as conn:
            return conn.execute(statement).scalar_one()