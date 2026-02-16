
class Soccer:
    def __init__(self):
        super().__init__()
        self.ball = True
        self.field = True
        self.players_by_team = 11

    def mejenga(self):
        if self.ball and self.field and self.players_by_team >= 11:
            print(
                f"Tengo ganas de mejenguear solo necesito los 11 del otro equipo para un reto")
        else:
            print(
                f"Aun no tengo todo lo que necesito para quitarme la fiebre de mejenguear")


class Volleyball:
    def __init__(self):
        super().__init__()
        self.ball = True
        self.net = True
        self.players_by_team = 6

    def volleyball_game(self):
        if self.ball and self.net and self.players_by_team >= 6:
            print(f"Voy a ir a jugar volley")
        else:
            print(f"Aun no tengo todo lo que necesito para ir a jugar Volley")


class Baseball:
    def __init__(self):
        super().__init__()
        self.ball = True
        self.bases = 3
        self.bat = 1
        self.players_by_team = 9

    def baseball_game(self):
        if self.ball and self.bases and self.bat >= 1 and self.players_by_team >= 9:
            print(f"Voy a ir a jugar Baseball")
        else:
            print(f"Aun no tengo todo lo que necesito para ir a jugar Volley")


class Olympic_Jump:
    def __init__(self):
        super().__init__()
        self.running_shoes = True
        self.pole_vault = True

    def jump(self):
        if self.running_shoes and self.pole_vault:
            print(f"Voy a entrenar fuerte saltar con garrocha")
        else:
            print(f"No tengo zapatos o palo")


class Athlete(Soccer, Volleyball, Baseball, Olympic_Jump):

    def __init__(self):
        super().__init__()

    def modify_amount_of_players(self, people):
        self.players_by_team = people

    def validate_pole_vault(self, pole_vault):
        self.pole_vault = pole_vault


# Notas importantes:
# 1 Al crear el metodo de modify en Athlete me permite modificar el total de jugadores porque sí hay atributos que se repiten, toma unicamente el de la primera clase. Podemos hacer lo mismo con todos los demas atributos
# 2 Es obligatorio inicializar super().__init__() en cada clase para que llame a la siguiente, caso contrario da error, o si no llamarlas explicitamente con Class.__init__(self)


person = Athlete()

print(person.players_by_team)
person.modify_amount_of_players(9)

print(person.players_by_team)
person.mejenga()

person.jump()
person.volleyball_game()
person.baseball_game()

person.validate_pole_vault(False)
person.jump()
