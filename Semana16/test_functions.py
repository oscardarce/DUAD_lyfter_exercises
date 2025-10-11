
import pytest
from functions3 import add_numbers_of_the_list
from functions4 import word_backwards
from functions5 import mayus_or_minus
from functions6 import sorted_word
from functions7 import prime_numbers

################3################

def test_add_numbers_of_the_list_functions_3():
    list_of_four_numbers = [4, 6, 2, 29]
    sum_list = sum(list_of_four_numbers) 
    sum_list_function = add_numbers_of_the_list(list_of_four_numbers)
    
    assert sum_list_function == sum_list
    

def test_add_numbers_of_the_list_fail_functions_3():
    list_of_four_numbers = [4, 6, 2, 29]
    list_of_three_numbers = [4, 2, 4, 79]
    total_of_list_of_three_numbers = add_numbers_of_the_list(list_of_three_numbers)
    
    if list_of_four_numbers != total_of_list_of_three_numbers:
        pytest.raises(AssertionError)

def test_add_numbers_of_the_list_functions_with_no_numbers():
    empty_list = []
    no_numbers = add_numbers_of_the_list(empty_list)
    zero = 0

    assert no_numbers == zero

################4################

def test_spell_word_backwards_functions_4():
    random_word = "Hola Mundo"
    result = word_backwards(random_word)

    assert result == "odnuM aloH"


def test_fail_spell_word_backwards_functions_4():
    random_number = 4
    
    with pytest.raises(TypeError):
        word_backwards(random_number)

def test_empty_spell_word_backwards_functions_4():
    random_word = ""
    result = word_backwards(random_word)
    
    assert result == random_word

################5################

def test_mayus_or_minus_functions_5():
    i_love_sushi_word = "I love Nación Sushi"
    mayus_result = 3
    minus_result = 13

    result_of_mayus = mayus_or_minus(i_love_sushi_word)
    assert result_of_mayus == (mayus_result,minus_result)


def test_mayus_or_minus_functions_5():
    i_love_sushi_word = "I love Nación Sushi"
    mayus_result = 3
    minus_result = 13

    result_of_mayus = mayus_or_minus(i_love_sushi_word)
    assert result_of_mayus == (mayus_result,minus_result)


def test_mayus_or_minus_number_error_functions_5():
    word_that_is_number = 123

    with pytest.raises(TypeError):
        mayus_or_minus(word_that_is_number)


def test_mayus_or_minus_empty_functions_5():
    i_love_sushi_word = ""
    
    mayus_result = 0
    minus_result = 0
    
    result_of_mayus = mayus_or_minus(i_love_sushi_word)

    assert result_of_mayus == (mayus_result,minus_result)

################6################

def test_sorted_words_functions6():
    
    words_for_change = "python-variable-funcion-computadora-monitor"
    result = sorted_word(words_for_change)      
    expected = "computadora-funcion-monitor-python-variable"      
    
    assert result == expected

def test_sorted_words_empty_functions6():
    words_for_change = ""
    result = sorted_word(words_for_change)      
    expected = ("")

    assert result == expected
    

def test_sorted_words_fail_functions6():
    words_for_change = 3
    
    with pytest.raises(TypeError):
        sorted_word(words_for_change)

################7################

def test_prime_numbers_functions7():
    list_of_numbers = [1, 4, 6, 7, 13, 9, 67]
    result = prime_numbers(list_of_numbers)
    
    expected = [7,13,67]
    
    assert result == expected
    
    
def test_prime_numbers_empty_list_functions7():
    nums = []
    result = prime_numbers(nums)
    assert result == []

    
def test_prime_numbers_contains_non_int_raises_type_error():

    with pytest.raises(TypeError):
        prime_numbers([2, "a", 3])