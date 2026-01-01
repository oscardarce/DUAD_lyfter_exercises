from logica.categories import Categoria


class Movimiento:
    def __init__(self, category: Categoria, movement_type, amount):
        self.category = category
        self.type = movement_type
        self.amount = amount
