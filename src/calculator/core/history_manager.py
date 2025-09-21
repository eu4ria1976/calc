"""
History Manager
Manages calculation history.
"""

from typing import List, Tuple
import json
import os


class HistoryManager:
    """Manager for calculation history"""
    
    def __init__(self, history_file: str = "calculator_history.json"):
        self.history_file = history_file
        self.history: List[Tuple[str, str]] = []  # List of (expression, result) tuples
        self.load_history()
    
    def add_entry(self, expression: str, result: str):
        """
        Add an entry to the history.
        
        Args:
            expression (str): The mathematical expression
            result (str): The result of the expression
        """
        self.history.append((expression, result))
        self.save_history()
    
    def get_history(self) -> List[Tuple[str, str]]:
        """
        Get the calculation history.
        
        Returns:
            List[Tuple[str, str]]: List of (expression, result) tuples
        """
        return self.history.copy()
    
    def clear_history(self):
        """Clear the calculation history"""
        self.history.clear()
        self.save_history()
    
    def save_history(self):
        """Save history to file"""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.history, f)
        except Exception:
            # If we can't save to file, just continue
            pass
    
    def load_history(self):
        """Load history from file"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    self.history = json.load(f)
        except Exception:
            # If we can't load from file, start with empty history
            self.history = []