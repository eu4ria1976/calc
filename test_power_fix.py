"""
Test script to verify the power function fix
"""
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from src.calculator.core.expression_parser import ExpressionParser
from src.calculator.core.calculator import CalculatorController

def test_power_functionality():
    """Test that power expressions work correctly"""
    print("Testing power functionality...")
    
    # Test with expression parser directly
    parser = ExpressionParser()
    
    # Test cases
    test_cases = [
        ("2^3", 8),
        ("3^2", 9),
        ("5^0", 1),
        ("2^8", 256),
        ("10^2", 100)
    ]
    
    print("Testing ExpressionParser with power operator:")
    for expression, expected in test_cases:
        try:
            result = parser.parse_and_evaluate(expression)
            if abs(result - expected) < 1e-10:
                print(f"  PASS: {expression} = {result}")
            else:
                print(f"  FAIL: {expression} = {result}, expected {expected}")
        except Exception as e:
            print(f"  ERROR: {expression} -> {str(e)}")
    
    # Test with calculator controller
    controller = CalculatorController()
    
    print("\nTesting CalculatorController with power expressions:")
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
    test_power_functionality()