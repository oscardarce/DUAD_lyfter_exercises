hello_world = "Hola Mundo"


def word_backwards(word):
    new_word_backwards = ""
    counter = len(word) - 1  
    
    for letters in word:
        new_word_backwards += word[counter] 
        
        print(word[counter], end="")
        counter = counter - 1
    

    return new_word_backwards


def main():
    word_backwards(hello_world)


main()
