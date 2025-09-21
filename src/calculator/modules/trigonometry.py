"""
Trigonometry Module for Scientific Calculator
Provides trigonometric functions including sin, cos, tan and their inverses/hyperbolic variants.
"""

import math
from typing import Union

Number = Union[int, float]

def sin(x: Number, degrees: bool = False) -> float:
    """
    Calculate sine of an angle.
    
    Args:
        x (Number): Angle in radians or degrees
        degrees (bool): If True, interpret x as degrees. Default is False (radians)
        
    Returns:
        float: Sine of the angle
        
    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    if degrees:
        x = math.radians(x)
        
    return math.sin(x)

def cos(x: Number, degrees: bool = False) -> float:
    """
    Calculate cosine of an angle.
    
    Args:
        x (Number): Angle in radians or degrees
        degrees (bool): If True, interpret x as degrees. Default is False (radians)
        
    Returns:
        float: Cosine of the angle
        
    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    if degrees:
        x = math.radians(x)
        
    return math.cos(x)

def tan(x: Number, degrees: bool = False) -> float:
    """
    Calculate tangent of an angle.
    
    Args:
        x (Number): Angle in radians or degrees
        degrees (bool): If True, interpret x as degrees. Default is False (radians)
        
    Returns:
        float: Tangent of the angle
        
    Raises:
        TypeError: If x is not a number
        ValueError: If the result is undefined (e.g., tan(90°))
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    if degrees:
        x = math.radians(x)
        
    # Check for undefined values (when cos(x) = 0)
    if abs(math.cos(x)) < 1e-15:
        raise ValueError("Tangent is undefined for this angle")
        
    return math.tan(x)

def asin(x: Number) -> float:
    """
    Calculate arc sine (inverse sine) of a value.
    
    Args:
        x (Number): Value in the range [-1, 1]
        
    Returns:
        float: Arc sine in radians
        
    Raises:
        TypeError: If x is not a number
        ValueError: If x is outside the valid range [-1, 1]
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1]")
        
    return math.asin(x)

def acos(x: Number) -> float:
    """
    Calculate arc cosine (inverse cosine) of a value.
    
    Args:
        x (Number): Value in the range [-1, 1]
        
    Returns:
        float: Arc cosine in radians
        
    Raises:
        TypeError: If x is not a number
        ValueError: If x is outside the valid range [-1, 1]
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1]")
        
    return math.acos(x)

def atan(x: Number) -> float:
    """
    Calculate arc tangent (inverse tangent) of a value.
    
    Args:
        x (Number): Any real number
        
    Returns:
        float: Arc tangent in radians
        
    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
        
    return math.atan(x)

def sinh(x: Number) -> float:
    """
    Calculate hyperbolic sine of a value.
    
    Args:
        x (Number): Any real number
        
    Returns:
        float: Hyperbolic sine
        
    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
        
    return math.sinh(x)

def cosh(x: Number) -> float:
    """
    Calculate hyperbolic cosine of a value.
    
    Args:
        x (Number): Any real number
        
    Returns:
        float: Hyperbolic cosine
        
    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
        
    return math.cosh(x)

def tanh(x: Number) -> float:
    """
    Calculate hyperbolic tangent of a value.
    
    Args:
        x (Number): Any real number
        
    Returns:
        float: Hyperbolic tangent
        
    Raises:
        TypeError: If x is not a number
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
        
    return math.tanh(x)