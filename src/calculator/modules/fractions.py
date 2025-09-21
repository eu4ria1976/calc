"""
Fractions Module for Scientific Calculator
Provides fraction operations including simplification and arithmetic operations.
"""

from fractions import Fraction
from typing import Union

Number = Union[int, float]

def simplify_fraction(numerator: int, denominator: int) -> tuple:
    """
    Simplify a fraction to its lowest terms.
    
    Args:
        numerator (int): Numerator of the fraction
        denominator (int): Denominator of the fraction
        
    Returns:
        tuple: Simplified fraction as (numerator, denominator)
        
    Raises:
        TypeError: If numerator or denominator is not an integer
        ValueError: If denominator is zero
    """
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Numerator and denominator must be integers")
    
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
        
    frac = Fraction(numerator, denominator)
    return (frac.numerator, frac.denominator)

def add_fractions(num1: int, den1: int, num2: int, den2: int) -> tuple:
    """
    Add two fractions.
    
    Args:
        num1 (int): Numerator of first fraction
        den1 (int): Denominator of first fraction
        num2 (int): Numerator of second fraction
        den2 (int): Denominator of second fraction
        
    Returns:
        tuple: Result of addition as (numerator, denominator)
        
    Raises:
        TypeError: If any input is not an integer
        ValueError: If any denominator is zero
    """
    if not all(isinstance(x, int) for x in [num1, den1, num2, den2]):
        raise TypeError("All inputs must be integers")
    
    if den1 == 0 or den2 == 0:
        raise ValueError("Denominators cannot be zero")
        
    frac1 = Fraction(num1, den1)
    frac2 = Fraction(num2, den2)
    result = frac1 + frac2
    return (result.numerator, result.denominator)

def subtract_fractions(num1: int, den1: int, num2: int, den2: int) -> tuple:
    """
    Subtract two fractions.
    
    Args:
        num1 (int): Numerator of first fraction
        den1 (int): Denominator of first fraction
        num2 (int): Numerator of second fraction
        den2 (int): Denominator of second fraction
        
    Returns:
        tuple: Result of subtraction as (numerator, denominator)
        
    Raises:
        TypeError: If any input is not an integer
        ValueError: If any denominator is zero
    """
    if not all(isinstance(x, int) for x in [num1, den1, num2, den2]):
        raise TypeError("All inputs must be integers")
    
    if den1 == 0 or den2 == 0:
        raise ValueError("Denominators cannot be zero")
        
    frac1 = Fraction(num1, den1)
    frac2 = Fraction(num2, den2)
    result = frac1 - frac2
    return (result.numerator, result.denominator)

def multiply_fractions(num1: int, den1: int, num2: int, den2: int) -> tuple:
    """
    Multiply two fractions.
    
    Args:
        num1 (int): Numerator of first fraction
        den1 (int): Denominator of first fraction
        num2 (int): Numerator of second fraction
        den2 (int): Denominator of second fraction
        
    Returns:
        tuple: Result of multiplication as (numerator, denominator)
        
    Raises:
        TypeError: If any input is not an integer
        ValueError: If any denominator is zero
    """
    if not all(isinstance(x, int) for x in [num1, den1, num2, den2]):
        raise TypeError("All inputs must be integers")
    
    if den1 == 0 or den2 == 0:
        raise ValueError("Denominators cannot be zero")
        
    frac1 = Fraction(num1, den1)
    frac2 = Fraction(num2, den2)
    result = frac1 * frac2
    return (result.numerator, result.denominator)

def divide_fractions(num1: int, den1: int, num2: int, den2: int) -> tuple:
    """
    Divide two fractions.
    
    Args:
        num1 (int): Numerator of first fraction
        den1 (int): Denominator of first fraction
        num2 (int): Numerator of second fraction
        den2 (int): Denominator of second fraction
        
    Returns:
        tuple: Result of division as (numerator, denominator)
        
    Raises:
        TypeError: If any input is not an integer
        ValueError: If any denominator is zero or if second fraction is zero
    """
    if not all(isinstance(x, int) for x in [num1, den1, num2, den2]):
        raise TypeError("All inputs must be integers")
    
    if den1 == 0 or den2 == 0:
        raise ValueError("Denominators cannot be zero")
        
    if num2 == 0:
        raise ValueError("Cannot divide by zero fraction")
        
    frac1 = Fraction(num1, den1)
    frac2 = Fraction(num2, den2)
    result = frac1 / frac2
    return (result.numerator, result.denominator)

def decimal_to_fraction(decimal: Number) -> tuple:
    """
    Convert a decimal to a fraction.
    
    Args:
        decimal (Number): Decimal number to convert
        
    Returns:
        tuple: Equivalent fraction as (numerator, denominator)
        
    Raises:
        TypeError: If decimal is not a number
    """
    if not isinstance(decimal, (int, float)):
        raise TypeError("Input must be a number")
        
    frac = Fraction(decimal).limit_denominator()
    return (frac.numerator, frac.denominator)