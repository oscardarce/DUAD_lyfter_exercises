from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base

DB_NAME = "Orm_Lyfter"
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"


class DbConnection:
    def __init__(self, db_name=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.engine = create_engine(self.build_uri())
        self.Session = sessionmaker(bind=self.engine)

    def build_uri(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

    def setup_database(self):
        exists = set(inspect(self.engine).get_table_names())

        Base.metadata.create_all(self.engine)

        for table in Base.metadata.tables.values():
            state = "ya existía" if table.name in exists else "creada"
            print(f"'{table.name}' : {state}")
