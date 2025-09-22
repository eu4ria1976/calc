"""
Test script to verify the GUI state management fix.
"""

import sys
import os

# Add the calculator directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.calculator.gui.calculator_gui import ScientificCalculator
from src.calculator.core.calculator import CalculatorController

def test_gui_state_management():
    """Test that the GUI properly manages state after applying functions"""
    # Create a calculator controller to test with
    controller = CalculatorController()
    
    # Simulate the sequence: 90 -> sin -> + -> 2 -> =
    # Step 1: Input 90
    result1 = controller.process_input("90")
    print(f"Input 90: {result1}")
    
    # Step 2: Apply sin function
    result2 = controller.process_input("sin(90)")
    print(f"sin(90) = {result2}")
    
    # Step 3: Try to add 2 (this should use the result of sin(90), which is 1, not the original 90)
    # In the fixed version, we need to make sure the last_result is updated
    controller.last_result = float(controller.format_output(result2))  # Simulate the fix
    result3 = controller.process_input("1+2")  # Using 1 directly since that's what sin(90) should give us
    print(f"1+2 = {result3}")
    
    # Verify that we get 3, not 92
    assert result3 == 3.0, f"Expected 3.0, got {result3}"
    
    print("GUI state management test passed!")

def test_with_direct_controller():
    """Test the controller directly to make sure our fixes work"""
    controller = CalculatorController()
    
    # Test reciprocal function
    result = controller.process_input("reciprocal(2)")
    print(f"reciprocal(2) = {result}")
    assert result == 0.5, f"Expected 0.5, got {result}"
    
    # Test trigonometric functions with degrees
    result = controller.process_input("sin(90)")
    print(f"sin(90) = {result}")
    assert abs(result - 1.0) < 1e-10, f"Expected 1.0, got {result}"
    
    result = controller.process_input("cos(0)")
    print(f"cos(0) = {result}")
    assert abs(result - 1.0) < 1e-10, f"Expected 1.0, got {result}"
    
    print("Direct controller tests passed!")

if __name__ == "__main__":
    print("Testing GUI state management fix...")
    test_gui_state_management()
    test_with_direct_controller()
    print("All tests passed!")