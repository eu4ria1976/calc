"""
Logarithms Module for Scientific Calculator
Provides logarithmic functions including natural log, log base 10, log base 2, and general logarithms.
"""

import math
from typing import Union

Number = Union[int, float]

def ln(x: Number) -> float:
    """
    Calculate natural logarithm (base e) of a number.
    
    Args:
        x (Number): Positive real number
        
    Returns:
        float: Natural logarithm of x
        
    Raises:
        TypeError: If x is not a number
        ValueError: If x is not positive
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    if x <= 0:
        raise ValueError("Input must be positive")
        
    return math.log(x)

def log10(x: Number) -> float:
    """
    Calculate logarithm base 10 of a number.
    
    Args:
        x (Number): Positive real number
        
    Returns:
        float: Logarithm base 10 of x
        
    Raises:
        TypeError: If x is not a number
        ValueError: If x is not positive
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    if x <= 0:
        raise ValueError("Input must be positive")
        
    return math.log10(x)

def log2(x: Number) -> float:
    """
    Calculate logarithm base 2 of a number.
    
    Args:
        x (Number): Positive real number
        
    Returns:
        float: Logarithm base 2 of x
        
    Raises:
        TypeError: If x is not a number
        ValueError: If x is not positive
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    if x <= 0:
        raise ValueError("Input must be positive")
        
    return math.log2(x)

def log(x: Number, base: Number = math.e) -> float:
    """
    Calculate logarithm of a number with a specified base.
    
    Args:
        x (Number): Positive real number
        base (Number): Positive real number, base of the logarithm (default is e for natural log)
        
    Returns:
        float: Logarithm of x with the specified base
        
    Raises:
        TypeError: If x or base is not a number
        ValueError: If x is not positive or base is not positive or base equals 1
    """
    if not isinstance(x, (int, float)) or not isinstance(base, (int, float)):
        raise TypeError("Inputs must be numbers")
    
    if x <= 0:
        raise ValueError("x must be positive")
        
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
        
    return math.log(x, base)