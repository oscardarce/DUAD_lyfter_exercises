hello_world = "Hola Mundo"


def word_backwards(word):
    new_word_backwards = ""
    counter = 0
    for letters in word:
        new_word_backwards = word[counter-1]
        counter = counter-1
        print(new_word_backwards, end="")


def main():
    word_backwards(hello_world)


main()
