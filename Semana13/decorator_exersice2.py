class Operations:
    def __init__(self):
        self.total = 0

    def only_numbers(func):

        def wrapper(self, *args, **kwargs):

            print("\nInicio del decorador")

            for number in args:
                if not isinstance(number, (int, float)):
                    raise TypeError(f"{number} no es número\n")

            for key, value in kwargs.items():
                if not isinstance(value, (int, float)):
                    raise TypeError(f"{key}={number} no es un número")

            result = func(self, *args, **kwargs)

            print(
                f"Estos son los argumentos: {args} y el fin del decorador\n ")
            return result
        return wrapper

    @only_numbers
    def add_numbers(self, *args, **kwargs):

        for number in args:
            self.total = self.total + number

        for key, value in kwargs.items():
            self.total = self.total + value
        print(f"El total de tu suma es de {self.total}")

    @only_numbers
    def subtract_numbers(self, *args,  **kwargs):

        for number in args:
            self.total = self.total - number

        for key, value in kwargs.items():
            self.total = self.total - value

        print(f"El total de tu resta es de {self.total}")

    @only_numbers
    def multiply_numbers(self, *args, **kwargs):

        for number in args:
            self.total = self.total * number

        for key, value in kwargs.items():
            self.total = self.total * value

        print(f"El total de tu multiplicación es de {self.total}")

    @only_numbers
    def divide_numbers(self, *args, **kwargs):

        for number in args:
            if number == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            self.total = self.total / number

        for key, value in kwargs.items():
            if value == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            self.total = self.total / value

        print(f"El total de tu división es de {self.total}")


basic_calculator = Operations()

basic_calculator.add_numbers(2, 4, 5, 6, 7, 8, number1=7, number2=1)
basic_calculator.subtract_numbers(2, 6, number1=7, number2=3)
basic_calculator.multiply_numbers(2, 3, number1=1, number4=4)
basic_calculator.divide_numbers(6, 4, number1="a", number3=3)
