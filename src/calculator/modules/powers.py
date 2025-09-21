"""
Powers Module for Scientific Calculator
Provides power and root functions including exponentiation, square root, cube root, and nth root.
"""

import math
from typing import Union

Number = Union[int, float]

def power(x: Number, y: Number) -> float:
    """
    Calculate x raised to the power of y (x^y).
    
    Args:
        x (Number): Base number
        y (Number): Exponent
        
    Returns:
        float: x raised to the power of y
        
    Raises:
        TypeError: If x or y is not a number
        ValueError: If x is negative and y is not an integer
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Inputs must be numbers")
    
    # Handle negative base with non-integer exponent
    if x < 0 and not isinstance(y, int):
        raise ValueError("Negative base with non-integer exponent is not supported")
        
    return math.pow(x, y)

def sqrt(x: Number) -> float:
    """
    Calculate square root of a number.
    
    Args:
        x (Number): Non-negative real number
        
    Returns:
        float: Square root of x
        
    Raises:
        TypeError: If x is not a number
        ValueError: If x is negative
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
        
    return math.sqrt(x)

def cbrt(x: Number) -> float:
    """
    Calculate cube root of a number.
    
    Args:
        x (Number): Any real number
        
    Returns:
        float: Cube root of x
        
    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    # Handle negative numbers correctly
    if x < 0:
        return -math.pow(-x, 1/3)
    else:
        return math.pow(x, 1/3)

def nth_root(x: Number, n: Number) -> float:
    """
    Calculate nth root of a number.
    
    Args:
        x (Number): Real number
        n (Number): Positive integer root
        
    Returns:
        float: nth root of x
        
    Raises:
        TypeError: If x or n is not a number
        ValueError: If n is not a positive integer or if x is negative and n is even
    """
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        raise TypeError("Inputs must be numbers")
    
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
        
    if x < 0 and n % 2 == 0:
        raise ValueError("Cannot calculate even root of negative number")
        
    # Handle negative numbers with odd roots
    if x < 0:
        return -math.pow(-x, 1/n)
    else:
        return math.pow(x, 1/n)

def exp(x: Number) -> float:
    """
    Calculate e raised to the power of x (e^x).
    
    Args:
        x (Number): Exponent
        
    Returns:
        float: e raised to the power of x
        
    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
        
    return math.exp(x)


def square(x: Number) -> float:
    """
    Calculate the square of a number (x^2).
    
    Args:
        x (Number): Base number
        
    Returns:
        float: x squared
        
    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
        
    return power(x, 2)

def cube(x: Number) -> float:
    """
    Calculate the cube of a number (x^3).
    
    Args:
        x (Number): Base number
        
    Returns:
        float: x cubed
        
    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
        
    return power(x, 3)