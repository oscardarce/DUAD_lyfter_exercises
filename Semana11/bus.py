
class Person():
    def __init__(self, name):
        self.name = name


class Bus:

    def __init__(self):
        self.max_passengers = 5
        self.total_of_passengers = 0

    def add_passengers(self, passenger):

        if passenger and self.total_of_passengers < 5:
            self.total_of_passengers = self.total_of_passengers + 1
            print(
                f"Recogiste un nuevo pasajero {passenger.name}, es tu pasajero número {self.total_of_passengers}")
        else:
            print(
                f"Haz alcanzado la capacidad maxima de pasajeros que es de {self.max_passengers}, {passenger.name} no puede subir")


bus = Bus()

passenger1 = Person("Oscar")
passenger2 = Person("Rodrigo")
passenger3 = Person("Karen")
passenger4 = Person("Andrea")
passenger5 = Person("Julio")
passenger6 = Person("Pablo")


bus.add_passengers(passenger1)
bus.add_passengers(passenger2)
bus.add_passengers(passenger3)
bus.add_passengers(passenger4)
bus.add_passengers(passenger5)
bus.add_passengers(passenger6)
