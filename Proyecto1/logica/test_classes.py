from category import Category
from movimiento import Movimiento

def test_movimiento_amount():
    movimiento = Movimiento(1500)
    assert movimiento.amount == 1500


def test_movimiento_amount_negative():
    movimiento = Movimiento(-500)
    assert movimiento.amount == -500


def test_category_name():
    categoria = Category("Alimentación")
    assert categoria.category == "Alimentación"


