from db_connection import ConnectionManager

class UserRepository:
    def __init__(self, db_manager: ConnectionManager):
        self.db = db_manager

    def add_user(self, first_name, email, username, password, birthdate, bank_account_state="active"):
        query = "INSERT INTO users (first_name, email, username, password, birthdate, bank_account_state) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;"
        try:
            self.db.cursor.execute(query, (first_name, email, username, password, birthdate, bank_account_state))
            user_id = self.db.cursor.fetchone()[0]
            self.db.connection.commit()
            return user_id
        except Exception as e:
            self.db.connection.rollback()
            print(f"Error adding user: {e}")
            return None

    def add_car(self, brand, model, year, state="available"):
        query = "INSERT INTO cars (brand, model, year, state) VALUES (%s, %s, %s, %s) RETURNING id;"
        try:
            self.db.cursor.execute(query, (brand, model, year, state))
            car_id = self.db.cursor.fetchone()[0]
            self.db.connection.commit()
            return car_id
        except Exception as e:
            self.db.connection.rollback()
            print(f"Error adding car: {e}")
            return None

    def create_rental(self, user_id, car_id):
        self.db.cursor.execute("SELECT state FROM cars WHERE id = %s;", (car_id,))
        car = self.db.cursor.fetchone()
        if not car or car[0] != "available":
            return None

        try:
            self.db.cursor.execute("INSERT INTO car_rental (id_user, id_car, rental_state) VALUES (%s, %s, 'active') RETURNING id;", (user_id, car_id))
            rental_id = self.db.cursor.fetchone()[0]
            self.db.cursor.execute("UPDATE cars SET state = 'rented' WHERE id = %s;", (car_id,))
            self.db.connection.commit()
            return rental_id
        except Exception as e:
            self.db.connection.rollback()
            print(f"Error creating rental: {e}")
            return None

    def update_user_state(self, user_id, new_state):
        try:
            self.db.cursor.execute("UPDATE users SET bank_account_state = %s WHERE id = %s;", (new_state, user_id))
            self.db.connection.commit()
            return True
        except Exception:
            self.db.connection.rollback()
            return False

    def update_car_state(self, car_id, new_state):
        try:
            self.db.cursor.execute("UPDATE cars SET state = %s WHERE id = %s;", (new_state, car_id))
            self.db.connection.commit()
            return True
        except Exception:
            self.db.connection.rollback()
            return False

    def update_rental_state(self, rental_id, new_state):
        try:
            self.db.cursor.execute("UPDATE car_rental SET rental_state = %s WHERE id = %s;", (new_state, rental_id))
            self.db.connection.commit()
            return True
        except Exception:
            self.db.connection.rollback()
            return False

    def complete_rental(self, rental_id):
        self.db.cursor.execute("SELECT id_car FROM car_rental WHERE id = %s AND rental_state != 'completed';", (rental_id,))
        rental = self.db.cursor.fetchone()
        if not rental: return False

        try:
            self.db.cursor.execute("UPDATE car_rental SET rental_state = 'completed' WHERE id = %s;", (rental_id,))
            self.db.cursor.execute("UPDATE cars SET state = 'available' WHERE id = %s;", (rental[0],))
            self.db.connection.commit()
            return True
        except Exception:
            self.db.connection.rollback()
            return False

    def get_filtered_data(self, table_name, filters_dict):
        allowed_tables = ['users', 'cars', 'car_rental']
        if table_name not in allowed_tables: return []

        query = f"SELECT * FROM {table_name}"
        params = []

        if filters_dict:
            conditions = []
            for column, value in filters_dict.items():
                conditions.append(f"{column} = %s")
                params.append(value)
            query += " WHERE " + " AND ".join(conditions)

        try:
            self.db.cursor.execute(query, tuple(params))
            columns = [desc[0] for desc in self.db.cursor.description]
            results = [dict(zip(columns, row)) for row in self.db.cursor.fetchall()]
            return results
        except Exception as e:
            print(f"Dynamic query error: {e}")
            return []