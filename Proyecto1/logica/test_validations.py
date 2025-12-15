from validations import validate_categories_exist, validate_movement_fields, validate_is_number


def test_validate_categories_exist_empty():
    data_categories = []
    result = validate_categories_exist(data_categories)
    assert result == False


def test_validate_categories_exist_not_empty():
    data_categories = ["Comida", "Salario"]
    result = validate_categories_exist(data_categories)
    assert result == True


def test_validate_movement_fields_empty_amount():
    result = validate_movement_fields("")
    assert result == False


def test_validate_movement_fields_non_numeric():
    result = validate_movement_fields("abc")
    assert result == False


def test_validate_movement_fields_negative_amount():
    result = validate_movement_fields("-500")
    assert result == False


def test_validate_movement_fields_valid_amount():
    result = validate_movement_fields("1000")
    assert result == True


def test_validate_is_number_empty():
    result = validate_is_number("")
    assert result == False


def test_validate_is_number_non_numeric():
    result = validate_is_number("abc")
    assert result == False


def test_validate_is_number_negative():
    result = validate_is_number("-1000")
    assert result == False


def test_validate_is_number_valid():
    result = validate_is_number("1500")
    assert result == True
