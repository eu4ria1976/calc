"""
Calculator Buttons Component
Handles the button panels of the calculator.
"""

import tkinter as tk


class CalculatorButtons:
    """Button component for the calculator"""
    
    def __init__(self, parent, button_callback):
        self.parent = parent
        self.button_callback = button_callback
        self.button_frame = None
        self.create_buttons()
    
    def create_buttons(self):
        """Create all calculator buttons"""
        # Button frame
        self.button_frame = tk.Frame(self.parent, bg="#f5f5f5")
        self.button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Configure grid weights for responsive design
        for i in range(10):  # Adjust based on actual number of rows
            self.button_frame.rowconfigure(i, weight=1)
        for i in range(10):  # Adjust based on actual number of columns
            self.button_frame.columnconfigure(i, weight=1)
        
        # Button definitions
        buttons = [
            # Row 1: Secondary functions
            [
                ("π", "pi", "secondary"),
                ("e", "e", "secondary"),
                ("C", "clear", "clear"),
                ("AC", "all_clear", "all_clear")
            ],
            # Row 2: Trigonometric functions
            [
                ("sin", "sin", "function"),
                ("cos", "cos", "function"),
                ("tan", "tan", "function"),
                ("asin", "asin", "function"),
                ("acos", "acos", "function"),
                ("atan", "atan", "function")
            ],
            # Row 3: Logarithmic functions
            [
                ("ln", "ln", "function"),
                ("log", "log10", "function"),
                ("log2", "log2", "function"),
                ("e^x", "exp", "function")
            ],
            # Row 4: Power/Root functions
            [
                ("x²", "square", "function"),
                ("x³", "cube", "function"),
                ("√x", "sqrt", "function"),
                ("∛x", "cbrt", "function"),
                ("x^y", "power", "operator")
            ],
            # Row 5: Factorial/Fraction functions
            [
                ("x!", "factorial", "function"),
                ("x!!", "double_factorial", "function"),
                ("1/x", "reciprocal", "function"),
                ("±", "toggle_sign", "function")
            ],
            # Row 6: Digits and basic operators
            [
                ("7", "7", "digit"),
                ("8", "8", "digit"),
                ("9", "9", "digit"),
                ("/", "/", "operator"),
                ("(", "(", "function"),
                (")", ")", "function")
            ],
            # Row 7: Digits and basic operators
            [
                ("4", "4", "digit"),
                ("5", "5", "digit"),
                ("6", "6", "digit"),
                ("*", "*", "operator")
            ],
            # Row 8: Digits and basic operators
            [
                ("1", "1", "digit"),
                ("2", "2", "digit"),
                ("3", "3", "digit"),
                ("-", "-", "operator")
            ],
            # Row 9: Digits and basic operators
            [
                ("0", "0", "digit"),
                (".", ".", "digit"),
                ("=", "=", "equals"),
                ("+", "+", "operator")
            ]
        ]
        
        # Create buttons
        for row_idx, row in enumerate(buttons):
            for col_idx, (text, command, btn_type) in enumerate(row):
                # Use a closure to capture the command correctly
                btn = tk.Button(
                    self.button_frame,
                    text=text,
                    command=lambda c=command: self.button_callback(c),
                    font=("Arial", 12, "bold"),
                    bg=self.get_button_color(btn_type),
                    fg="white" if btn_type in ["operator", "function", "equals", "all_clear"] else "black",
                    activebackground=self.get_button_active_color(btn_type),
                    relief="raised",
                    bd=1
                )
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)
    
    def get_button_color(self, btn_type):
        """Get button color based on type"""
        colors = {
            "digit": "#f0f0f0",
            "operator": "#ff9500",
            "function": "#4a4a4a",
            "equals": "#34c759",
            "clear": "#ff3b30",
            "all_clear": "#ff3b30",
            "secondary": "#d0d0d0"
        }
        return colors.get(btn_type, "#f0f0f0")
    
    def get_button_active_color(self, btn_type):
        """Get button active color based on type"""
        colors = {
            "digit": "#e0e0e0",
            "operator": "#ffad33",
            "function": "#5a5a5a",
            "equals": "#4cd975",
            "clear": "#ff4d6d",
            "all_clear": "#ff4d6d",
            "secondary": "#c0c0c0"
        }
        return colors.get(btn_type, "#e0e0e0")