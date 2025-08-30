class Operations:
    def __init__(self):
        self.total = 0

    def only_numbers(func):

        def wrapper(self, *args, **kwargs):

            print("\nInicio del decorador")

            for number in args:
                if not isinstance(number, (int, float)):
                    raise ValueError(f"{number} no es número\n")

            func(self, *args, **kwargs)

            print(
                f"Estos son los argumentos: {args} y el fin del decorador\n ")

        return wrapper

    @only_numbers
    def add_numbers(self, *args):

        for number in args:
            self.total = self.total + number

        print(f"El total de tu suma es de {self.total}")

    @only_numbers
    def subtract_numbers(self, *args):

        for number in args:
            self.total = self.total - number

        print(f"El total de tu resta es de {self.total}")

    @only_numbers
    def multiply_numbers(self, *args):

        for number in args:
            self.total = self.total * number

        print(f"El total de tu multiplicación es de {self.total}")

    @only_numbers
    def divide_numbers(self, *args):

        for number in args:
            self.total = self.total / number

        print(f"El total de tu división es de {self.total}")


basic_calculator = Operations()

basic_calculator.add_numbers(2, 4, 5, 6, 7, 8)
basic_calculator.subtract_numbers(2, 6)
basic_calculator.multiply_numbers(2, 3)
basic_calculator.divide_numbers(6, 4)
