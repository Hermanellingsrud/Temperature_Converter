from temp_app.converter import celsius_to_fahrenheit, is_fever, is_valid_temp

# Test conversion from Celsius to Fahrenheit
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(37) == 98.6
    assert celsius_to_fahrenheit(0) == 32.0

# Test fever detection
def test_is_fever():
    assert is_fever(37.9) == False
    assert is_fever(38.1) == True

# Test if temperature is within valid range
def test_valid_range():
    assert is_valid_temp(30.0) == True
    assert is_valid_temp(45.0) == True
    assert is_valid_temp(29.9) == False
