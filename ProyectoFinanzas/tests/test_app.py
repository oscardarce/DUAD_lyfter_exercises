import pytest
from logica.movement import Movement
from logica.finance_manager import FinanceManager


# Verificar que se puede crear una categoría con un nombre
def test_create_category_with_name():
    app = FinanceManager()
    result = app.create_category("Comida")

    assert result == True
    assert "Comida" in app.get_category_names()


# Verificar que no se pueda agregar una categoría sin nombre
def test_validate_no_empty_category():
    app = FinanceManager()
    result = app.create_category("")

    assert result == False
    assert len(app.get_category_names()) == 0


# Verificar que se puede agregar una categoría al gestor
def test_add_category_to_app():
    app = FinanceManager()
    result = app.create_category("Comida")

    assert result == True
    assert "Comida" in app.get_category_names()


# Verificar que no se pueda agregar una categoría sin nombre
def test_validate_no_empty_category():
    app = FinanceManager()
    result = app.create_category("")

    assert result == False
    assert len(app.get_category_names()) == 0


# Prueba 7: Verificar que NO se puede agregar una categoría que ya existe"""
def test_no_category_duplicated():
    app = FinanceManager()
    app.create_category("Comida")
    result = app.create_category("Comida")

    assert result == False
    assert len(app.get_category_names()) == 1


# Verificar que se puede crear un gasto con datos válidos
def test_create_valid_expense():
    app = FinanceManager()
    app.create_category("Comida")
    result = app.create_expense("Comida", 50.0)

    assert result == True
    assert len(app.movements) == 1
    assert app.movements[0].amount == 50.0


# Verificar que NO se puede crear un gasto con monto negativo
def test_not_create_negative_expense():

    app = FinanceManager()
    app.create_category("Comida")
    result = app.create_expense("Comida", -50.0)

    # Verificar que el gasto NO se creó
    assert result == False
    assert len(app.movements) == 0


# Verificar que se puede crear un ingreso con datos válidos
def test_create_valid_income():
    app = FinanceManager()
    app.create_category("Salario")
    result = app.create_income("Salario", 5000.0)

    # Verificar que el ingreso se creó correctamente
    assert result == True
    assert len(app.movements) == 1
    assert app.movements[0].amount == 5000.0
    assert app.movements[0].type == "Ingreso"


# Verificar que se puede crear un movimiento de tipo Gasto"""
def test_create_valid_expense_movement():
    movement = Movement("Comida", "Gasto", 100.0)

    assert movement.category == "Comida"
    assert movement.type == "Gasto"
    assert movement.amount == 100.0

# Prueba 4: Verificar que se puede crear un movimiento de tipo Ingreso"""
def test_create_valid_income_movement():
    movement = Movement("Salario", "Ingreso", 5000.0)

    assert movement.category == "Salario"
    assert movement.type == "Ingreso"
    assert movement.amount == 5000.0
