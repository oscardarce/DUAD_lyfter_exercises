import FreeSimpleGUI as sg
from logica.categories import Categoria
from logica.movement import Movimiento


class GestorFinanzas:

    def __init__(self):
        self.categories: list[Categoria] = []
        self.movements: list[Movimiento] = []

    def create_category(self, name):
        name = name.strip()
        if not name:
            sg.popup_error("El nombre de la categoría no puede estar vacío")
            return False

        if self.get_category(name):
            sg.popup_error(f"La categoría {name} ya existe")
            return False

        self.categories.append(Categoria(name))
        return True

    def get_category(self, name):
        for category in self.categories:
            if category.name == name:
                return category
        return None

    def get_category_names(self):
        category_names = []

        for category in self.categories:
            category_names.append(category.name)

        return category_names

    def create_expense(self, category_name, amount):
        category = self.get_category(category_name)
        if not category:
            sg.popup_error("La categoría seleccionada no existe")
            return False

        try:
            amount_float = float(amount)
            if amount_float <= 0:
                sg.popup_error("El monto debe ser mayor a 0")
                return False
        except ValueError:
            sg.popup_error("El monto debe ser un número válido")
            return False

        self.movements.append(
            Movimiento(category, "Gasto", amount_float)
        )
        return True

    def create_income(self, category_name, amount):
        category = self.get_category(category_name)
        if not category:
            sg.popup_error("La categoría seleccionada no existe")
            return False

        try:
            amount_float = float(amount)
            if amount_float <= 0:
                sg.popup_error("El monto debe ser mayor a 0")
                return False
        except ValueError:
            sg.popup_error("El monto debe ser un número válido")
            return False

        self.movements.append(
            Movimiento(category, "Ingreso", amount_float)
        )
        return True

    def get_table_data(self):
        data_table = []

        for movement in self.movements:
            fila = [
                movement.category.name,
                movement.type,
                f"{movement.amount:.2f}"
            ]
            data_table.append(fila)

        return data_table
