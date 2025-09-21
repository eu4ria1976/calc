#!/usr/bin/env python3
"""
Test script to verify basic arithmetic operations
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from src.calculator.core.calculator import CalculatorController

def test_basic_operations():
    """Test basic arithmetic operations"""
    print("Testing basic arithmetic operations...")
    
    controller = CalculatorController()
    
    # Test cases for basic operations
    test_cases = [
        ("2 + 3", 5),
        ("10 - 4", 6),
        ("5 * 6", 30),
        ("20 / 4", 5),
        ("2 + 3 * 4", 14),  # Test order of operations
        ("(2 + 3) * 4", 20),  # Test parentheses
        ("10 / 2 + 3", 8),
        ("2 ^ 3", 8),  # Test power operator
    ]
    
    print("Testing CalculatorController with basic expressions:")
    for expression, expected in test_cases:
        try:
            result = controller.process_input(expression)
            if isinstance(result, (int, float)) and abs(result - expected) < 1e-10:
                print(f"  PASS: {expression} = {result}")
            else:
                print(f"  FAIL: {expression} = {result}, expected {expected}")
        except Exception as e:
            print(f"  ERROR: {expression} -> {str(e)}")

if __name__ == "__main__":
    test_basic_operations()