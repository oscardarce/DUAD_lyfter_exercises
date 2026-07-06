from typing import Optional, List
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email_address: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(20))

    cars: Mapped[List["Car"]] = relationship(back_populates="owner")
    addresses: Mapped[List["Address"]] = relationship(back_populates="owner")


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # permitido: auto sin dueño
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    brand: Mapped[str] = mapped_column(String(30), nullable=False)
    model: Mapped[str] = mapped_column(String(30), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)

    owner: Mapped[Optional["User"]] = relationship(back_populates="cars")


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # user id obligatorio: no existe dirección sin dueño
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    street: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(10), nullable=False)

    owner: Mapped["User"] = relationship(back_populates="addresses")