"""
Scientific Calculator Application
Main application file that initializes the GUI and integrates all components.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
import sys
import os

# Add the calculator directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import controller and GUI components
from core.calculator import CalculatorController
from gui.display import CalculatorDisplay
from gui.buttons import CalculatorButtons


class ScientificCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Scientific Calculator")
        self.window.geometry("400x600")
        self.window.minsize(400, 500)
        self.window.configure(bg="#f5f5f5")
        
        # Initialize controller
        self.controller = CalculatorController()
        
        # Calculator state
        self.current_input = ""
        self.reset_next = False
        
        # Create GUI components
        self.display = CalculatorDisplay(self.window)
        self.buttons = CalculatorButtons(self.window, self.handle_button_click)
        
        # Bind keyboard events
        self.bind_keyboard_events()
    
    def handle_button_click(self, command):
        """Handle button clicks"""
        try:
            if command in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self.append_digit(command)
            elif command == ".":
                self.append_decimal()
            elif command in ["+", "-", "*", "/"]:
                self.append_operator(command)
            elif command == "=":
                self.calculate()
            elif command == "clear":
                self.clear_input()
            elif command == "all_clear":
                self.all_clear()
            elif command == "pi":
                self.append_constant("π")
            elif command == "e":
                self.append_constant("e")
            elif command == "(":
                self.append_parenthesis("(")
            elif command == ")":
                self.append_parenthesis(")")
            elif command == "toggle_sign":
                self.toggle_sign()
            elif command in ["sin", "cos", "tan", "asin", "acos", "atan", "ln", "log10", "log2",
                            "exp", "sqrt", "cbrt", "square", "cube", "factorial", "double_factorial", "reciprocal"]:
                self.apply_function(command)
            elif command == "power":
                self.append_operator("^")
            elif command == "delete":
                self.delete_last_character()
            elif command == "percentage":
                self.apply_percentage()
            else:
                # For other commands, treat as expression
                self.current_input = command
                self.calculate()
        except Exception as e:
            self.show_error(str(e))
    
    def append_digit(self, digit):
        """Append a digit to the current input"""
        if self.reset_next:
            self.current_input = ""
            self.reset_next = False
        
        self.current_input += digit
        self.display.update_display(self.current_input)
    
    def append_decimal(self):
        """Append a decimal point to the current input"""
        if self.reset_next:
            self.current_input = "0"
            self.reset_next = False
        
        # Prevent multiple decimal points in a number
        if "." not in self.current_input.split()[-1]:
            if not self.current_input:
                self.current_input = "0."
            else:
                self.current_input += "."
            self.display.update_display(self.current_input)
    
    def append_operator(self, operator):
        """Append an operator to the current input"""
        if self.reset_next:
            self.current_input = str(self.controller.last_result)
            self.reset_next = False
        
        # Prevent consecutive operators
        if self.current_input and self.current_input[-1] in "+-*/":
            self.current_input = self.current_input[:-1] + operator
        else:
            self.current_input += operator
        
        self.display.update_display(self.current_input)
    
    def append_parenthesis(self, paren):
        """Append a parenthesis to the current input"""
        if self.reset_next:
            self.current_input = ""
            self.reset_next = False
        
        self.current_input += paren
        self.display.update_display(self.current_input)
    
    def append_constant(self, constant):
        """Append a mathematical constant to the current input"""
        if self.reset_next:
            self.current_input = ""
            self.reset_next = False
        
        if constant == "π":
            self.current_input += str(math.pi)
        elif constant == "e":
            self.current_input += str(math.e)
        
        self.display.update_display(self.current_input)
    
    def apply_function(self, func_name):
        """Apply a mathematical function to the current input or last result"""
        try:
            # If there's current input, use it
            if self.current_input:
                expression = f"{func_name}({self.current_input})"
            else:
                # If no input, apply function to 0
                expression = f"{func_name}(0)"
            
            # Process through controller
            result = self.controller.process_input(expression)
            
            # Format output
            formatted_result = self.controller.format_output(result)
            
            # Update display with result
            self.current_input = formatted_result
            self.display.update_display(self.current_input)
            self.reset_next = True
            
            # Update last result for subsequent operations
            try:
                self.controller.last_result = float(formatted_result)
            except ValueError:
                # If conversion fails, keep the previous last_result
                pass
            
        except Exception as e:
            self.show_error(str(e))
    
    def toggle_sign(self):
        """Toggle the sign of the current input or last result"""
        try:
            if self.current_input:
                if self.current_input.startswith("-"):
                    self.current_input = self.current_input[1:]
                else:
                    self.current_input = "-" + self.current_input
            else:
                self.controller.last_result = -self.controller.last_result
                self.current_input = str(self.controller.last_result)
            
            self.display.update_display(self.current_input)
        except Exception as e:
            self.show_error(str(e))
    
    def delete_last_character(self):
        """Delete the last character from the current input"""
        try:
            if self.current_input:
                self.current_input = self.current_input[:-1]
                if not self.current_input:
                    self.display.update_display("0")
                else:
                    self.display.update_display(self.current_input)
        except Exception as e:
            self.show_error(str(e))
    
    def apply_percentage(self):
        """Apply percentage in the context of an operation"""
        try:
            # If there's current input, check if it's part of an operation
            if self.current_input:
                # Check if the input contains an operator
                if any(op in self.current_input for op in ["+", "-", "*", "/"]):
                    # Parse the expression to get the operator and operands
                    # Find the last operator
                    last_operator_pos = -1
                    last_operator = None
                    for i in range(len(self.current_input) - 1, -1, -1):
                        if self.current_input[i] in "+-*/":
                            last_operator_pos = i
                            last_operator = self.current_input[i]
                            break
                    
                    if last_operator_pos != -1:
                        # Split the expression into first operand, operator, and second operand
                        first_operand_str = self.current_input[:last_operator_pos]
                        second_operand_str = self.current_input[last_operator_pos + 1:]
                        
                        try:
                            first_operand = float(first_operand_str)
                            second_operand = float(second_operand_str)
                            
                            # Calculate percentage based on the operator
                            if last_operator == "*":
                                # For multiplication, calculate first_operand * (second_operand%)
                                # This means first_operand * (second_operand / 100)
                                result = first_operand * (second_operand / 100)
                                self.current_input = str(result)
                                self.display.update_display(self.current_input)
                                self.reset_next = True
                                
                                # Update last result for subsequent operations
                                self.controller.last_result = result
                            elif last_operator == "/":
                                # For division, calculate first_operand / (second_operand%)
                                # This means first_operand / (second_operand / 100)
                                result = first_operand / (second_operand / 100)
                                self.current_input = str(result)
                                self.display.update_display(self.current_input)
                                self.reset_next = True
                                
                                # Update last result for subsequent operations
                                self.controller.last_result = result
                            elif last_operator == "+":
                                # For addition, calculate first_operand + (second_operand% of first_operand)
                                percentage_value = first_operand * (second_operand / 100)
                                result = first_operand + percentage_value
                                self.current_input = str(result)
                                self.display.update_display(self.current_input)
                                self.reset_next = True
                                
                                # Update last result for subsequent operations
                                self.controller.last_result = result
                            elif last_operator == "-":
                                # For subtraction, calculate first_operand - (second_operand% of first_operand)
                                percentage_value = first_operand * (second_operand / 100)
                                result = first_operand - percentage_value
                                self.current_input = str(result)
                                self.display.update_display(self.current_input)
                                self.reset_next = True
                                
                                # Update last result for subsequent operations
                                self.controller.last_result = result
                            
                            self.display.update_display(self.current_input)
                        except ValueError:
                            self.show_error("Invalid input for percentage")
                    else:
                        # No operator found, just convert the current input to percentage
                        try:
                            value = float(self.current_input)
                            result = value / 100
                            self.current_input = str(result)
                            self.display.update_display(self.current_input)
                            self.reset_next = True
                        except ValueError:
                            self.show_error("Invalid input for percentage")
                else:
                    # No operator in input, just convert the current input to percentage
                    try:
                        value = float(self.current_input)
                        result = value / 100
                        self.current_input = str(result)
                        self.display.update_display(self.current_input)
                        self.reset_next = True
                    except ValueError:
                        self.show_error("Invalid input for percentage")
            else:
                # If no input, apply percentage to last result
                result = self.controller.last_result / 100
                self.current_input = str(result)
                self.display.update_display(self.current_input)
                self.reset_next = True
                
                # Update last result for subsequent operations
                self.controller.last_result = result
        except Exception as e:
            self.show_error(str(e))
    
    def clear_input(self):
        """Clear the current input"""
        self.current_input = ""
        self.display.update_display("0")
    
    def all_clear(self):
        """Reset the calculator to initial state"""
        self.current_input = ""
        self.controller.last_result = 0
        self.reset_next = False
        self.display.clear_display()
    
    def calculate(self):
        """Evaluate the current expression"""
        try:
            if not self.current_input:
                return
            
            # Process input through controller
            result = self.controller.process_input(self.current_input)
            
            # Format output
            formatted_result = self.controller.format_output(result)
            
            # Update display
            self.display.update_display(formatted_result)
            self.reset_next = True
            
        except Exception as e:
            self.show_error(str(e))
    
    def show_error(self, message):
        """Show an error message"""
        self.display.update_display("Error")
        self.current_input = ""
        self.reset_next = True
        # Show error dialog
        messagebox.showerror("Calculation Error", message)
    
    def bind_keyboard_events(self):
        """Bind keyboard events for calculator input"""
        self.window.bind("<Key>", self.on_key_press)
        self.window.focus_set()
    
    def on_key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        keysym = event.keysym
        
        # Handle digits
        if key.isdigit():
            self.append_digit(key)
        # Handle operators
        elif key in "+-*/":
            self.append_operator(key)
        # Handle decimal point
        elif key == ".":
            self.append_decimal()
        # Handle Enter/Return for equals
        elif keysym in ["Return", "KP_Enter"]:
            self.calculate()
        # Handle Escape for all clear
        elif keysym == "Escape":
            self.all_clear()
        # Handle Backspace for clear
        elif keysym == "BackSpace":
            self.clear_input()
        # Handle parentheses
        elif key in "()":
            self.append_parenthesis(key)
    
    def run(self):
        """Run the calculator application"""
        self.window.mainloop()



if __name__ == "__main__":
    calculator = ScientificCalculator()
    calculator.run()