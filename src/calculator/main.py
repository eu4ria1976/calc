"""
Scientific Calculator Application
Main entry point that initializes and runs the calculator application.
"""

import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.calculator_gui import ScientificCalculator


def main():
    """Main entry point for the calculator application"""
    calculator = ScientificCalculator()
    calculator.run()


if __name__ == "__main__":
    main()