"""
Test script to check precision issues with trigonometric functions.
"""

import sys
import os

# Add the calculator directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.calculator.core.calculator import CalculatorController

def test_precision_issues():
    """Test precision issues with trigonometric functions"""
    calc = CalculatorController()
    
    # Test cases that should be zero
    test_cases = [
        ("cos(90)", 0.0),
        ("sin(360)", 0.0),
        ("tan(360)", 0.0),
        ("cos(270)", 0.0),
        ("sin(180)", 0.0),
        ("tan(180)", 0.0)
    ]
    
    print("Testing precision issues:")
    for expression, expected in test_cases:
        result = calc.process_input(expression)
        formatted_result = calc.format_output(result)
        print(f"{expression} = {formatted_result} (raw: {result})")
        
        # Check if the formatted result is "0"
        if formatted_result == "0":
            print(f"  -> Correctly formatted as zero")
        else:
            print(f"  -> Not formatted as zero")
        print()

if __name__ == "__main__":
    test_precision_issues()