import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        pi = math.pi
        result = (self.radius ** 2) * pi
        print(
            f"El radio del circulo es de {self.radius}, y su area es de: {result}")


circle1 = Circle(5)
circle2 = Circle(24)

circle1.calculate_area()
circle2.calculate_area()
