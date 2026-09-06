from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Administrator(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String)


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String)
    invoices: Mapped[list["Invoice"]] = relationship(
        back_populates="client",
        passive_deletes=True,
    )


# Tabla de productos (Frutas)
class Fruit(Base):
    __tablename__ = "fruits"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    date_of_entry: Mapped[date] = mapped_column(Date)
    quantity: Mapped[int]
    invoice_items: Mapped[list["InvoiceItem"]] = relationship(
        back_populates="product",
        passive_deletes=True,
    )


class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(
        # ondelete="RESTRICT": la base de datos impide borrar un cliente que ya tiene facturas asociadas
        ForeignKey("clients.id", ondelete="RESTRICT"),
        index=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    total: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    client: Mapped[Client] = relationship(back_populates="invoices")
    items: Mapped[list["InvoiceItem"]] = relationship(
        back_populates="invoice",
        cascade="all, delete-orphan",
    )


class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    invoice_id: Mapped[int] = mapped_column(
        ForeignKey("invoices.id", ondelete="CASCADE"),
        index=True,
    )
    fruit_id: Mapped[int] = mapped_column(
        # RESTRICT: no se puede borrar un producto que ya aparece en alguna facturas
        ForeignKey("fruits.id", ondelete="RESTRICT")
    )
    product_name: Mapped[str] = mapped_column(String(30))
    quantity: Mapped[int]
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    subtotal: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    invoice: Mapped[Invoice] = relationship(back_populates="items")
    product: Mapped[Fruit] = relationship(back_populates="invoice_items")
