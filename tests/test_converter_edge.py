from temp_app.converter import celsius_to_fahrenheit, is_fever, is_valid_temp

def test_celsius_edge_cases():
    # Extreme values
    assert round(celsius_to_fahrenheit(-273.15), 2) == -459.67 # absolute zero
    assert celsius_to_fahrenheit(1000) == 1832.0
    
    # Boundary values
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    
    # Decimal / negative
    assert celsius_to_fahrenheit(37.5) == 99.5
    assert celsius_to_fahrenheit(-40) == -40.0  # same in C and F

def test_is_fever_edge():
    assert is_fever(37.9) == False  # just below
    assert is_fever(38.0) == False  # at boundary
    assert is_fever(38.1) == True   # just above

def test_is_valid_temp_edge():
    assert is_valid_temp(30.0) == True   # lower bound
    assert is_valid_temp(45.0) == True   # upper bound
    assert is_valid_temp(29.9) == False  # just below
    assert is_valid_temp(45.1) == False  # just above
