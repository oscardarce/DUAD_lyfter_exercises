from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey


metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email_address", String(255), nullable=False, unique=True),
    Column("phone_number", String(20)),
)

# user_id NULL admitido (auto sin dueño)
cars_table = Table(
    "cars",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", ForeignKey("users.id", ondelete="SET NULL"), nullable=True),
    Column("brand", String(30), nullable=False),
    Column("model", String(30), nullable=False),
    Column("year", Integer, nullable=False),
)

# user_id obligatorio (no existe dirección sin dueño)
addresses_table = Table(
    "addresses",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", ForeignKey("users.id"), nullable=False),
    Column("street", String(255), nullable=False),
    Column("city", String(100), nullable=False),
    Column("zip_code", String(10), nullable=False),
)
