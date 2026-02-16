from abc import ABC, abstractmethod
import math


class Shape(ABC):

    def __init__(self, user_number):
        super().__init__()
        self._area = user_number
        self._perimeter = user_number

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        super().__init__(radius)
        self.__pi = math.pi

    def calculate_area(self):
        self._area = (self._area ** 2) * self.__pi
        print(f"El area de tu círculo es de {self._area}")

    def calculate_perimeter(self):
        self._perimeter = 2 * self.__pi * self._perimeter
        print(f"El perimetro de tu circulo es de {self._perimeter}")


class Square(Shape):
    def __init__(self, side):
        super().__init__(side)

    def calculate_area(self):
        self._area = self._area * self._area
        print(f"El área de tu cuadrado es de {self._area}")

    def calculate_perimeter(self):
        self._perimeter = self._perimeter * 4
        print(f"El perimetro de tu cuadrado es de {self._perimeter}")


class Rectangle(Shape):

    def __init__(self, user_number, height):
        super().__init__(user_number)
        self.__height = height

    def calculate_area(self):
        # Toca pasar area a ser ancho (width) y alto (height)
        self._area = self._area * self.__height
        print(f"El área de tu rectangulo es de {self._area}")

    def calculate_perimeter(self):
        # Lo mismo para el perimetro
        self._perimeter = 2 * (self._perimeter * self.__height)
        print(f"El perímetro de tu rectangulo es de {self._perimeter}")


circle = Circle(5)
circle.calculate_area()
circle.calculate_perimeter()
square = Square(5)
square.calculate_area()
square.calculate_perimeter()
rectangle = Rectangle(2, 4)
rectangle.calculate_area()
rectangle.calculate_perimeter()
