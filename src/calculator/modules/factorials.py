"""
Factorials Module for Scientific Calculator
Provides factorial functions including standard factorial, double factorial, and gamma function.
"""

import math
from typing import Union

Number = Union[int, float]

def factorial(n: int) -> int:
    """
    Calculate factorial of a non-negative integer (n!).
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
        
    return math.factorial(n)

def double_factorial(n: int) -> int:
    """
    Calculate double factorial of a non-negative integer (n!!).
    For even n: n!! = n * (n-2) * (n-4) * ... * 2
    For odd n: n!! = n * (n-2) * (n-4) * ... * 1
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Double factorial of n
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
        
    if n == 0 or n == 1:
        return 1
        
    result = 1
    while n > 1:
        result *= n
        n -= 2
        
    return result

def gamma(x: Number) -> float:
    """
    Calculate gamma function of a number.
    For positive integers: gamma(n) = (n-1)!
    
    Args:
        x (Number): Real number (except non-positive integers)
        
    Returns:
        float: Gamma function of x
        
    Raises:
        TypeError: If x is not a number
        ValueError: If x is a non-positive integer
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    # Check if x is a non-positive integer
    if isinstance(x, int) and x <= 0:
        raise ValueError("Gamma function is undefined for non-positive integers")
        
    return math.gamma(x)