
import pytest
from functions3 import add_numbers_of_the_list
from functions4 import word_backwards
from functions5 import mayus_or_minus
from functions6 import sorted_word
from functions7 import prime_numbers



def test_add_numbers_of_the_list_functions_3():
    list_of_four_numbers = [4, 6, 2, 29]
    total = sum(list_of_four_numbers) 
    all_numbers_of_the_list_added = add_numbers_of_the_list(list_of_four_numbers)
    
    assert all_numbers_of_the_list_added == total


def test_spell_word_backwards_functions_4():
    random_word = "Hola Mundo"
    result = word_backwards(random_word)
    assert result == "odnuM aloH"


def test_mayus_or_minus_functions_5():
    i_love_sushi_word = "I love Nación Sushi"
    mayus_result = 3
    minus_result = 13

    result_of_mayus = mayus_or_minus(i_love_sushi_word)
    assert result_of_mayus == (mayus_result,minus_result)


def test_sorted_words_functions6():
    
        words_for_change = "python-variable-funcion-computadora-monitor"
        result = sorted_word(words_for_change)
        
        expected = "computadora-funcion-monitor-python-variable"
        
        assert result == expected


def test_sorted_words_functions7():
    print("Falta implementar")