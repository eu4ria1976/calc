#!/usr/bin/env python3
"""
Test script to verify error handling
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from src.calculator.core.calculator import CalculatorController

def test_error_handling():
    """Test error handling for invalid inputs"""
    print("Testing error handling...")
    
    controller = CalculatorController()
    
    # Test cases for error handling
    test_cases = [
        "5 / 0",  # Division by zero
        "sqrt(-1)",  # Square root of negative number
        "ln(-5)",  # Natural log of negative number
        "factorial(-1)",  # Factorial of negative number
        "2 + ",  # Incomplete expression
        "2 + * 3",  # Invalid expression
        "unknown_function(5)",  # Unknown function
    ]
    
    print("Testing CalculatorController with invalid expressions:")
    for expression in test_cases:
        try:
            result = controller.process_input(expression)
            if isinstance(result, str) and result.startswith("Error"):
                print(f"  PASS: {expression} -> correctly caught error")
            else:
                print(f"  FAIL: {expression} = {result}, expected error")
        except Exception as e:
            print(f"  PASS: {expression} -> Exception caught: {str(e)}")

if __name__ == "__main__":
    test_error_handling()