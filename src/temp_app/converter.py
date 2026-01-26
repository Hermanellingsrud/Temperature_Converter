
#Temperature Converter Module
#Provides functions to convert between Celsius, Fahrenheit, and Kelvin.

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    Args:
    celsius (float): Temperature in Celsius
    Returns:
    float: Temperature in Fahrenheit
    Example:
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(100)
    212.0
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    Args:
    fahrenheit (float): Temperature in Fahrenheit
    Returns:
    float: Temperature in Celsius
    Example:
    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(212)
    100.0
    """
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin.
    Args:
    celsius (float): Temperature in Celsius
    Returns:
    float: Temperature in Kelvin
    Example:
    >>> celsius_to_kelvin(0)
    273.15
    """
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    Args:
    kelvin (float): Temperature in Kelvin
    Returns:
    float: Temperature in Celsius
    Example:
    >>> kelvin_to_celsius(273.15)
    0.0
    """
    return kelvin - 273.15

def celsius_to_rankine(celsius):
    """
    Convert temperature from Celsius to Rankine.
    Formula: Rankine = (Celsius + 273.15) × 9/5
    Args:
    celsius (float): Temperature in Celsius
    Returns:
    float: Temperature in Rankine
    Example:
    >>> celsius_to_rankine(0)
    491.67
    """
    kelvin = celsius_to_kelvin(celsius)
    return kelvin * 9/5

def rankine_to_celsius(rankine):
    """
    Convert temperature from Rankine to Celsius.
    Formula: Celsius = (Rankine × 5/9) - 273.15
    Args:
    rankine (float): Temperature in Rankine
    Returns:
    float: Temperature in Celsius
    Example:
    >>> rankine_to_celsius(491.67)
    0.0
    """
    kelvin = rankine * 5/9
    return kelvin_to_celsius(kelvin)

if __name__ == "__main__":
    # Quick test of conversion functions
    print("Temperature Converter Tests")
    print(f"0°C = {celsius_to_fahrenheit(0)}°F")
    print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    print(f"0°C = {celsius_to_kelvin(0)}K")
    print(f"0°C = {celsius_to_rankine(0)}°R")
    print(f"491.67°R = {rankine_to_celsius(491.67)}°C")
