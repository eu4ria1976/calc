"""
Utility Functions
Helper functions for the calculator application.
"""

import math
from typing import Union


def format_number(num: Union[int, float]) -> str:
    """
    Format a number for display.
    
    Args:
        num (Union[int, float]): Number to format
        
    Returns:
        str: Formatted number
    """
    if isinstance(num, int):
        return str(num)
    elif isinstance(num, float):
        # If it's a whole number, display as integer
        if num.is_integer():
            return str(int(num))
        else:
            # Format with up to 10 significant digits
            return f"{num:.10g}"
    else:
        return str(num)


def validate_numeric_input(value: str) -> bool:
    """
    Validate if a string represents a valid numeric input.
    
    Args:
        value (str): String to validate
        
    Returns:
        bool: True if valid numeric input, False otherwise
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_integer_value(num: float) -> bool:
    """
    Check if a float value is actually an integer.
    
    Args:
        num (float): Number to check
        
    Returns:
        bool: True if the number is an integer value, False otherwise
    """
    return num.is_integer()


def clamp_value(value: float, min_val: float, max_val: float) -> float:
    """
    Clamp a value between a minimum and maximum.
    
    Args:
        value (float): Value to clamp
        min_val (float): Minimum value
        max_val (float): Maximum value
        
    Returns:
        float: Clamped value
    """
    return max(min_val, min(value, max_val))


def to_degrees(radians: float) -> float:
    """
    Convert radians to degrees.
    
    Args:
        radians (float): Angle in radians
        
    Returns:
        float: Angle in degrees
    """
    return math.degrees(radians)


def to_radians(degrees: float) -> float:
    """
    Convert degrees to radians.
    
    Args:
        degrees (float): Angle in degrees
        
    Returns:
        float: Angle in radians
    """
    return math.radians(degrees)