"""
Test script to verify power functions in the calculator
"""

import sys
import os

# Add the calculator directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.calculator.core.calculator import CalculatorController

def test_power_functions():
    """Test the power functions through the calculator controller"""
    controller = CalculatorController()
    
    # Test square function
    print("Testing square function:")
    result = controller.process_input("square(4)")
    print(f"square(4) = {result}")
    
    result = controller.process_input("square(-3)")
    print(f"square(-3) = {result}")
    
    # Test cube function
    print("\nTesting cube function:")
    result = controller.process_input("cube(3)")
    print(f"cube(3) = {result}")
    
    result = controller.process_input("cube(-2)")
    print(f"cube(-2) = {result}")
    
    # Test power function through expression evaluation
    print("\nTesting power through expression evaluation:")
    result = controller.process_input("2**3")
    print(f"2**3 = {result}")
    
    result = controller.process_input("4**0.5")
    print(f"4**0.5 = {result}")

if __name__ == "__main__":
    test_power_functions()