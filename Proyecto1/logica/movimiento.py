from db import data_categories


class Expense():
    def __init__(self, expense_name, amount):
        self.expense_name = expense_name
        self.amount = amount


class Income():
    def __init__(self, income_name, amount):
        self.income_name = income_name
        self.amount = amount
