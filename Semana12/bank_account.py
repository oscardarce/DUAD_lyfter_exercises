class BankAccount:

    def __init__(self):
        self._balance = 0

    def add_money(self, amount):
        self._balance = self._balance + amount
        return self._balance

    def subtract(self, amount):
        self._balance = self._balance - amount
        return self._balance

    def show_balance(self):
        print(f"El saldo de tu cuenta es de {self._balance}")


class SavingsAccount(BankAccount):

    def __init__(self):
        super().__init__()
        self.__min_balance = 0

    def subtract(self, amount):
        if self._balance - amount < self.__min_balance:
            print("No puedes retirar más de lo que tienes en tu cuenta")
        else:
            self._balance = self._balance - amount


account = SavingsAccount()

account.add_money(50)
account.add_money(100)
account.subtract(500)

account.show_balance()
