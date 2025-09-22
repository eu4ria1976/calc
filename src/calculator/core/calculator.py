"""
Calculator Controller
Handles input processing, expression evaluation, and output formatting.
"""

import math
import sys
import os
from typing import Union

# Add the calculator directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import mathematical modules
from modules.trigonometry import sin, cos, tan, asin, acos, atan
from modules.logarithms import ln, log10, log2
from modules.powers import power, sqrt, cbrt, exp, square, cube, reciprocal
from modules.factorials import factorial, double_factorial
from modules.fractions import simplify_fraction, add_fractions, subtract_fractions, multiply_fractions, divide_fractions


class CalculatorController:
    """Controller class for handling calculator operations"""
    
    def __init__(self):
        self.last_result = 0
        self.history = []
    
    def process_input(self, input_str: str) -> Union[float, str]:
        """
        Process user input and return the result.
        
        Args:
            input_str (str): User input string
            
        Returns:
            Union[float, str]: Result of the calculation or error message
        """
        try:
            # If input is a function call, process it directly
            if self._is_function_call(input_str):
                return self._evaluate_function(input_str)
            
            # Otherwise, evaluate as a mathematical expression
            return self._evaluate_expression(input_str)
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _is_function_call(self, input_str: str) -> bool:
        """Check if input is a function call"""
        functions = [
            "sin", "cos", "tan", "asin", "acos", "atan",
            "ln", "log10", "log2", "exp", "sqrt", "cbrt",
            "factorial", "double_factorial", "square", "cube", "power", "reciprocal"
        ]
        return any(input_str.startswith(func + "(") for func in functions)
    
    def _evaluate_function(self, input_str: str) -> float:
        """Evaluate a function call"""
        try:
            # Remove spaces
            input_str = input_str.replace(" ", "")
            
            # Extract function name and argument
            func_name = input_str.split("(")[0]
            arg_str = input_str[len(func_name)+1:-1]  # Remove function name and parentheses
            
            # Evaluate argument
            arg = self._evaluate_expression(arg_str)
            
            # Apply function
            if func_name == "sin":
                return sin(arg, degrees=True)
            elif func_name == "cos":
                return cos(arg, degrees=True)
            elif func_name == "tan":
                return tan(arg, degrees=True)
            elif func_name == "asin":
                return asin(arg)
            elif func_name == "acos":
                return acos(arg)
            elif func_name == "atan":
                return atan(arg)
            elif func_name == "ln":
                return ln(arg)
            elif func_name == "log10":
                return log10(arg)
            elif func_name == "log2":
                return log2(arg)
            elif func_name == "exp":
                return exp(arg)
            elif func_name == "sqrt":
                return sqrt(arg)
            elif func_name == "cbrt":
                return cbrt(arg)
            elif func_name == "factorial":
                return factorial(int(arg))
            elif func_name == "double_factorial":
                return double_factorial(int(arg))
            elif func_name == "square":
                return square(arg)
            elif func_name == "cube":
                return cube(arg)
            elif func_name == "power":
                # For power function, we need to parse two arguments
                # This is a special case as it needs to be handled differently
                # We'll handle this in the GUI by creating an expression like "power(x,y)"
                # But for direct function calls, we need to parse the arguments
                raise ValueError("Power function requires two arguments, use expression evaluation instead")
            elif func_name == "reciprocal":
                return reciprocal(arg)
            else:
                raise ValueError(f"Unknown function: {func_name}")
        except (TypeError, ValueError) as e:
            raise ValueError(f"Error in function {func_name}: {str(e)}")
    
    def _evaluate_expression(self, expression: str) -> float:
        """
        Evaluate a mathematical expression.
        
        Args:
            expression (str): Mathematical expression to evaluate
            
        Returns:
            float: Result of the evaluation
        """
        # Replace constants
        expression = expression.replace("pi", str(math.pi))
        expression = expression.replace("e", str(math.e))
        
        # For security, we'll only allow safe operations
        # Replace power operator
        expression = expression.replace("^", "**")
        # In a real application, you would want to use a proper expression parser

        allowed_chars = set("0123456789+-*/^().e ")
        allowed_chars = set("0123456789+-*/().e ")
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Invalid characters in expression")
        
        # Evaluate the expression
        try:
            result = eval(expression)
            self.last_result = result
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")
    
    def format_output(self, result: Union[float, str]) -> str:
        """
        Format the output for display.
        
        Args:
            result (Union[float, str]): Result to format
            
        Returns:
            str: Formatted result
        """
        if isinstance(result, str):
            return result
        elif isinstance(result, (int, float)):
            # Format numbers nicely
            # Handle precision issues with trigonometric functions
            if abs(result) < 1e-10:
                return "0"
            elif result == int(result):
                return str(int(result))
            else:
                return f"{result:.10g}"
        else:
            return str(result)
    
    def get_history(self) -> list:
        """Get calculation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()