i_love_sushi_word = "I love Nación Sushi"

# Mi solución


def mayus_or_minus(word):

    new_word_without_spaces = word.replace(" ", "")
    counter_mayus = 0
    counter_min = 0

    for letter in new_word_without_spaces:
        if letter.isupper():
            counter_mayus = counter_mayus + 1
        if letter.islower():
            counter_min = counter_min + 1

    print(f"Tienes {counter_mayus} letras mayusculas")
    print(f"Tienes {counter_min} letras minusculas")


mayus_or_minus(i_love_sushi_word)

# Método 1
# RegEx can be used to check if a string contains the specified search pattern.

# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"planet$"
# *	Zero or more occurrences	"he.*o"
# +	One or more occurrences	"he.+o"
# ?	Zero or one occurrences	"he.?o"
# {}	Exactly the specified number of occurrences	"he.{2}o"
# |	Either or	"falls|stays"
# ()	Capture and group


# Método 2 comprensión de listas:

# def number_of_minus_mayus(word):
#    mayus = len([letter for letter in word if letter.isupper()])
#    minus = len([letter for letter in word if letter.islower()])

#    print(f"Hay un total de: {mayus} letras mayusculas")
#    print(f"Hay un total de: {minus} letras minusculas")


# def main(word):
#    number_of_minus_mayus(word)


# main(i_love_sushi_word)

# https://www.youtube.com/watch?v=JYmgIMfKjTQ
# [nuevo_elemento for elemento in iterable if condición]
