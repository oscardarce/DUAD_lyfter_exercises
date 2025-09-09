week = {
    "Lunes": 1,
    "Martes": 2,
    "Miercoles": 3,
    "Jueves": 4,
    "Viernes": 5,
    "Sabado": 6,
    "Domingo": 7
}


def only_week_days(func):

    def wrapper(*args, **kwargs):

        print("Inicio del decorador")

        for day in args:
            if not isinstance(day, int) or day not in week.values():
                print(f"{day} no es un día válido de la semana\n")
                return None

        func(*args, **kwargs)
        print(
            f"Estos son los argumentos: {args} y el fin del decorador\n ")

    return wrapper


@only_week_days
def number_picker(*args):
    for day in args:
        for key, value in week.items():
            if value == day:
                print(f"Este es el día: {key}")
                return key


number_picker(1, 3, 5, 7)
number_picker(1, "hola", 20, 3)
number_picker(1, 20, 3)
