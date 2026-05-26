import psycopg2
import os
import json

DB_NAME = "lyfter_car_rental"
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"

class ConnectionManager:

    def __init__(self, db_name=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.create_connection()
        if self.connection:
            print("Te has conectado a la base de datos de Lyfter Car Rental")
            self.cursor = self.connection.cursor()

            self.setup_database()

            mock_cars = self.load_mock_data("mock_car_data.json")
            mock_users = self.load_mock_data("mock_user_data.json")

            # Insertamos los datos en la base de datos
            self.seed_database(mock_users, mock_cars)

    def create_connection(self):
        try:
            connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return connection
        except Exception as error:
            print("Error connecting to the database: ", error)
            return None

    def close_connection(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()
        print("Se cerró la conexión")

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()
        print("Query executed")

        if self.cursor.description:
            return self.cursor.fetchall()
        return None

    def setup_database(self):
        self.cursor.execute("DROP TABLE IF EXISTS car_rental CASCADE;")
        self.cursor.execute("DROP TABLE IF EXISTS cars CASCADE;")
        self.cursor.execute("DROP TABLE IF EXISTS users CASCADE;")

        self.cursor.execute("SET DateStyle TO 'MDY';")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                email VARCHAR(50),
                username VARCHAR(50),
                password VARCHAR(50),
                birthdate DATE,
                bank_account_state TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                id SERIAL PRIMARY KEY,
                brand VARCHAR(50),
                model VARCHAR(50),
                year INTEGER,
                state VARCHAR(50)
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS car_rental (
                id SERIAL PRIMARY KEY,
                id_user INT REFERENCES users(id),
                id_car INT REFERENCES cars(id),
                rental_date DATE DEFAULT CURRENT_DATE,
                rental_state VARCHAR(50)
            );
        """)
        self.connection.commit()

    def load_mock_data(self, mock_data_filename):
        mock_data_path = os.path.join(os.path.dirname(__file__), mock_data_filename)
        try:
            with open(mock_data_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta {mock_data_path}")
            return None
        except json.JSONDecodeError:
            print(f"Error: El archivo {mock_data_filename} no es un JSON válido.")
            return None

    def seed_database(self, mock_users, mock_cars):
        if mock_users:
            user_query = """
                INSERT INTO users (first_name, email, username, password, birthdate, bank_account_state)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            for user in mock_users:
                self.cursor.execute(user_query, (
                    user.get("first_name"), user.get("email"), user.get("username"),
                    user.get("password"), user.get("birthdate"), user.get("bank_account_state")
                ))
            print(f"Inserted {len(mock_users)} mock users.")

        if mock_cars:
            car_query = """
                INSERT INTO cars (brand, model, year, state)
                VALUES (%s, %s, %s, %s)
            """
            for car in mock_cars:
                self.cursor.execute(car_query, (
                    car.get("brand"), car.get("model"), car.get("year"), "available"
                ))
            print(f"Inserted {len(mock_cars)} mock cars.")

        self.connection.commit()