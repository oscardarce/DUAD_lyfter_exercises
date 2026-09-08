from sqlalchemy import URL, create_engine, inspect
from sqlalchemy.orm import sessionmaker

from models import Base


DB_NAME = "authentication"
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = 5432


class DbConnection:
    def __init__(
        self,
        db_name=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    ):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.engine = create_engine(self.build_uri())
        # expire_on_commit. False, el objeto conserva los valores que tenía en memoria al hacer el commit
        self.Session = sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )

    def build_uri(self):
        # URL.create (escapa caracteres especiales en usuario/password)
        return URL.create(
            drivername="postgresql+psycopg2",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.db_name,
        )

    def setup_database(self):
        # create_all crea solo las tablas que falten no toca las que ya existen
        existing_tables = set(inspect(self.engine).get_table_names())
        Base.metadata.create_all(self.engine)

        for table in Base.metadata.sorted_tables:
            state = "ya existía" if table.name in existing_tables else "creada"
            print(f"'{table.name}': {state}")
