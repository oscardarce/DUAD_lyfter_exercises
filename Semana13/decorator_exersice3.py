import datetime

current_date = datetime.date.today()


class User:
    def __init__(self, year, month, day):
        self.date_of_birth = datetime.date(year, month, day)
        self.age = 0


def validate_is_adult(func):

    def wrapper(self, *args):

        self.age = current_date.year - self.date_of_birth.year

        if self.age < 18:
            raise ValueError(
                "Eres menor de edad,no puedes tomar alcohol aun")

        func(self, *args)

    return wrapper


@validate_is_adult
def drink_beer(user: User):
    print(
        f"\nTu fecha de nacimiento es {user.date_of_birth} y tienes una edad de {user.age}, puedes beber alcohol\n")


patricia = User(2010, 9, 3)
oscar = User(1994, 9, 3)

drink_beer(oscar)
drink_beer(patricia)
