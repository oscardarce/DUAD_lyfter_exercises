words_for_change = "python-variable-funcion-computadora-monitor"


def sorted_word(word):
    splitted_word = word.split("-")
    print(splitted_word)
    sorted_word = sorted(splitted_word)
    print(sorted_word)
    result = "-".join(sorted_word)
    print(result)


sorted_word(words_for_change)
