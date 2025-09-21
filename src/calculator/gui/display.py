"""
Calculator Display Component
Handles the display area of the calculator.
"""

import tkinter as tk


class CalculatorDisplay:
    """Display component for the calculator"""
    
    def __init__(self, parent):
        self.parent = parent
        self.display_var = tk.StringVar(value="0")
        self.display = None
        self.create_display()
    
    def create_display(self):
        """Create the calculator display area"""
        # Display frame
        display_frame = tk.Frame(self.parent, height=60, bg="#1e1e1e", relief="solid", bd=2)
        display_frame.pack(fill=tk.X, padx=10, pady=10)
        display_frame.pack_propagate(False)
        
        # Main display
        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Courier", 18, "bold"),
            bg="#1e1e1e",
            fg="#ffffff",
            anchor="e",
            padx=10
        )
        self.display.pack(fill=tk.BOTH, expand=True)
    
    def update_display(self, value):
        """Update the display with a new value"""
        # Format large numbers in scientific notation to prevent overflow
        if isinstance(value, str) and len(value) > 15:
            try:
                # Try to convert to float to check if it's a number
                num_value = float(value)
                # For very large numbers, use scientific notation
                if abs(num_value) >= 1e10 or (abs(num_value) < 1e-4 and num_value != 0):
                    formatted_value = f"{num_value:.6e}"
                else:
                    formatted_value = value
            except ValueError:
                # If it's not a number, just use the original value
                formatted_value = value
        else:
            formatted_value = value
        
        self.display_var.set(formatted_value)
    
    def get_display_value(self):
        """Get the current display value"""
        return self.display_var.get()
    
    def clear_display(self):
        """Clear the display"""
        self.display_var.set("0")