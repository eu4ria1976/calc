"""
Test script to verify the fixes for the "1/x" function and trigonometric functions.
"""

import sys
import os

# Add the calculator directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.calculator.core.calculator import CalculatorController

def test_reciprocal():
    """Test the reciprocal function"""
    calc = CalculatorController()
    
    # Test reciprocal of 2 (should be 0.5)
    result = calc.process_input("reciprocal(2)")
    print(f"reciprocal(2) = {result}")
    assert result == 0.5, f"Expected 0.5, got {result}"
    
    # Test reciprocal of 0.5 (should be 2)
    result = calc.process_input("reciprocal(0.5)")
    print(f"reciprocal(0.5) = {result}")
    assert result == 2.0, f"Expected 2.0, got {result}"
    
    # Test reciprocal of -4 (should be -0.25)
    result = calc.process_input("reciprocal(-4)")
    print(f"reciprocal(-4) = {result}")
    assert result == -0.25, f"Expected -0.25, got {result}"
    
    print("All reciprocal tests passed!")

def test_trigonometric_degrees():
    """Test that trigonometric functions use degrees by default"""
    calc = CalculatorController()
    
    # Test sin(90) = 1 (degrees)
    result = calc.process_input("sin(90)")
    print(f"sin(90) = {result}")
    assert abs(result - 1.0) < 1e-10, f"Expected 1.0, got {result}"
    
    # Test cos(0) = 1 (degrees)
    result = calc.process_input("cos(0)")
    print(f"cos(0) = {result}")
    assert abs(result - 1.0) < 1e-10, f"Expected 1.0, got {result}"
    
    # Test tan(45) = 1 (degrees)
    result = calc.process_input("tan(45)")
    print(f"tan(45) = {result}")
    assert abs(result - 1.0) < 1e-10, f"Expected 1.0, got {result}"
    
    # Test sin(30) = 0.5 (degrees)
    result = calc.process_input("sin(30)")
    print(f"sin(30) = {result}")
    assert abs(result - 0.5) < 1e-10, f"Expected 0.5, got {result}"
    
    print("All trigonometric tests passed!")

if __name__ == "__main__":
    print("Testing fixes...")
    test_reciprocal()
    test_trigonometric_degrees()
    print("All tests passed!")