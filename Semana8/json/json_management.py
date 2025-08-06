import json

json_file_path = "pokemons.json"


def load_data(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_data(path):
    pokemons = load_data(json_file_path)

    keep_iterating = True
    print("Por favor ingresa el pokemón que deseas registrar.")

    # Pedir datos del pokemon al usuario
    while keep_iterating:
        name = input("Por favor ingresa el nombre de tu pokemon:\n").strip()
        while not name:
            name = input(
                "Necesitas el nombre de tu pokemon:\n").strip()

        pokemon_type = input(
            "Por favor ingresa el tipo de tu pokemon:\n").strip()
        while not pokemon_type:
            pokemon_type = input(
                "Necesitas el tipo de tu pokemon:\n").strip()

        print("Ingresa los atributos de tu pokemon")

        while True:
            try:
                hp_attribute = int(input("HP:\n"))
                while hp_attribute <= 0:
                    hp_attribute = int(
                        input("HP invalida por favor ingresa el HP de tú pokemon:\n"))

                attack_attribute = int(
                    input("Ataque:\n"))
                while attack_attribute <= 0:
                    attack_attribute = int(
                        input("Ataque invalido por favor ingresa el ataque de tú pokemon:\n"))

                defense_attribute = int(input("Defensa:\n"))
                while defense_attribute <= 0:
                    defense_attribute = int(
                        input("Defensa invalida por favor ingresa la defensa de tú pokemon:\n"))

                sp_attack_attribute = int(input("Ataque Especial:\n"))
                while sp_attack_attribute <= 0:
                    sp_attack_attribute = int(input(
                        "Ataque especial invalido, por favor ingresa el ataque especial de tu pokemon\n"))

                sp_defense_attribute = int(input("Defensa Especial:\n"))
                while sp_defense_attribute <= 0:
                    sp_defense_attribute = int(input(
                        "Defensa especial invalida, por favor ingresa la defensa especial de tu pokemon\n"))

                speed_attribute = int(input("Velocidad:\n"))
                while speed_attribute <= 0:
                    speed_attribute = int(input(
                        "Velocidad invalida, por favor ingresa la velicidad de tu pokemon\n"))
                break
            except ValueError:
                print("Ingresa un número valido")
                continue

        new_pokemon = {
            "name": {
                "english": name
            },
            "type": [pokemon_type],
            "base": {
                "HP": hp_attribute,
                "Attack": attack_attribute,
                "Defense": defense_attribute,
                "Sp. Attack": sp_attack_attribute,
                "Sp. Defense": sp_defense_attribute,
                "Speed": speed_attribute
            }
        }

        # Escribir la data en el JSON
        pokemons.append(new_pokemon)

        # Validar continuar o salir.
        while True:
            try:
                validate_continue = int(
                    input("¿Deseas agregar otro pokémon digita 1.Sí o 2.No?\n"))
                if validate_continue == 2:
                    keep_iterating = False
                    break
                elif validate_continue == 1:
                    break
                else:
                    print("Ingresa solo 1 o 2.")
            except ValueError:
                print("Por favor ingresa un número válido.")

    # Guardar Pokemones en el JSON
    with open(path, "w", encoding="utf-8") as file:
        json.dump(pokemons, file, indent=2)
        print("Datos guardados correctamente.")


write_data(json_file_path)
