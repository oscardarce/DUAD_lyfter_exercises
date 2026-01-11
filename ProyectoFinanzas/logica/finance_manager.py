from logica.movement import Movement


class FinanceManager:

    def __init__(self):
        self.categories: list = []
        self.movements: list[Movement] = []

    def create_category(self, name):
        name = name.strip()
        if not name:
            return False

        if self.get_category(name):
            return False

        self.categories.append(name)
        return True

    def get_category(self, name):
        if name in self.categories:
            return name
        else:
            return None

    def get_category_names(self):
        return self.categories

    def create_expense(self, category_name, amount, description):
        category = self.get_category(category_name)
        if not category:
            return False
        if not description:
            return False

        try:
            amount_float = float(amount)
            if amount_float <= 0:
                return False
        except ValueError:
            return False

        self.movements.append(
            Movement(category, "Gasto", amount_float, description)
        )
        return True

    def create_income(self, category_name, amount, description):
        category = self.get_category(category_name)
        if not category:
            return False
        if not description:
            return False

        try:
            amount_float = float(amount)
            if amount_float <= 0:
                return False
        except ValueError:
            return False

        self.movements.append(
            Movement(category, "Ingreso", amount_float, description)
        )
        return True

    def get_table_data(self):
        data_table = []

        for movement in self.movements:
            fila = [
                movement.category,
                movement.type,
                f"{movement.amount:.2f}",
                movement.description
            ]
            data_table.append(fila)

        return data_table
