import pytest
import random
from sort import sort_numbers_asc

number_list_one = list(range(-200,200))
random_list = random.sample(number_list_one, k=200)

number_list_two = [-2, -3, -1, 1, -4, 3, 4, 5, 6]
number_list_three = []

error = "Hola"

def test_sort_numbers_asc_with_small_list():

    expected_list = [-4, -3, -2, -1, 1, 3, 4, 5, 6]
    expected_ordered_lists = sort_numbers_asc(number_list_two)

    assert expected_list == expected_ordered_lists


def test_sort_numbers_asc_with_empty_list():
    
    expected_list = number_list_three
    expected_ordered_lists = sort_numbers_asc(number_list_three)

    assert expected_list == expected_ordered_lists


def test_sort_numbers_asc_with_big_list():

    expected_list = sort_numbers_asc(random_list)

    assert random_list == expected_list


def test_try_sort_numbers_asc_with_no_list_item():

    with pytest.raises(TypeError):
        sort_numbers_asc("Hola")