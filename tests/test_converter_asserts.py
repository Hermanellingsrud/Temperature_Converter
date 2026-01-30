from temp_app.converter import celsius_to_fahrenheit

def test_assert_examples():
    # Example input
    temp = 37
    result = celsius_to_fahrenheit(temp)
    message = "Conversion completed successfully"
    temps = [37.0, 38.1]

    # Simple assertions
    assert result == 98.6               # Value equality
    assert temp > 0                      # Comparison
    assert "error" not in message        # String does not contain
    assert temps == [37.0, 38.1]         # List equality

    # With messages
    assert result == 98.6, "Conversion failed"

    # Multiple conditions
    assert 0 <= temp <= 40               # Valid range
