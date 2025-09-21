#!/usr/bin/env python3
"""
Test script to verify the x^y button functionality
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from src.calculator.core.calculator import CalculatorController
from src.calculator.modules.powers import power

def test_xy_button():
    """Test the x^y button functionality"""
    print("Testing x^y button functionality...")
    
    # Test the power function directly
    print("Testing power function directly:")
    test_cases = [
        (2, 3, 8),
        (3, 2, 9),
        (5, 0, 1),
        (2, 8, 256),
        (10, 2, 100),
        (2.5, 2, 6.25),
        (4, 0.5, 2),  # Square root
        (-2, 3, -8),  # Negative base with odd exponent
    ]
    
    for x, y, expected in test_cases:
        try:
            result = power(x, y)
            if abs(result - expected) < 1e-10:
                print(f"  PASS: {x}^{y} = {result}")
            else:
                print(f"  FAIL: {x}^{y} = {result}, expected {expected}")
        except Exception as e:
            print(f"  ERROR: {x}^{y} -> {str(e)}")
    
    # Test through the calculator controller
    print("\nTesting through calculator controller:")
    controller = CalculatorController()
    
    # Test cases using the ^ operator
    expression_cases = [
        ("2^3", 8),
        ("3^2", 9),
        ("5^0", 1),
        ("2^8", 256),
        ("10^2", 100),
        ("2.5^2", 6.25),
    ]
    
    for expression, expected in expression_cases:
        try:
            result = controller.process_input(expression)
            if isinstance(result, (int, float)) and abs(result - expected) < 1e-10:
                print(f"  PASS: {expression} = {result}")
            else:
                print(f"  FAIL: {expression} = {result}, expected {expected}")
        except Exception as e:
            print(f"  ERROR: {expression} -> {str(e)}")

if __name__ == "__main__":
    test_xy_button()