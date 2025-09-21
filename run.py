#!/usr/bin/env python3
"""
Scientific Calculator Application
Main entry point script for running the calculator application.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from calculator.main import main

if __name__ == "__main__":
    main()