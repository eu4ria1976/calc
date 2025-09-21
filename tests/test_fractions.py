"""
Unit tests for the fractions module.
"""

import unittest
from src.calculator.modules.fractions import *

class TestFractions(unittest.TestCase):
    """Test cases for fraction functions."""
    
    def test_simplify_fraction(self):
        """Test fraction simplification."""
        self.assertEqual(simplify_fraction(4, 8), (1, 2))
        self.assertEqual(simplify_fraction(0, 5), (0, 1))
        self.assertEqual(simplify_fraction(7, 1), (7, 1))
        self.assertEqual(simplify_fraction(10, 15), (2, 3))
        self.assertEqual(simplify_fraction(-4, 8), (-1, 2))
        self.assertEqual(simplify_fraction(4, -8), (-1, 2))
    
    def test_simplify_fraction_invalid(self):
        """Test fraction simplification with invalid inputs."""
        with self.assertRaises(ValueError):
            simplify_fraction(1, 0)
        with self.assertRaises(TypeError):
            simplify_fraction(1.5, 2)
        with self.assertRaises(TypeError):
            simplify_fraction(1, "invalid")
        with self.assertRaises(TypeError):
            simplify_fraction("invalid", 2)
    
    def test_add_fractions(self):
        """Test fraction addition."""
        self.assertEqual(add_fractions(1, 2, 1, 3), (5, 6))
        self.assertEqual(add_fractions(1, 4, 1, 4), (1, 2))
        self.assertEqual(add_fractions(0, 1, 1, 2), (1, 2))
    
    def test_add_fractions_invalid(self):
        """Test fraction addition with invalid inputs."""
        with self.assertRaises(ValueError):
            add_fractions(1, 0, 1, 2)
        with self.assertRaises(ValueError):
            add_fractions(1, 2, 1, 0)
        with self.assertRaises(TypeError):
            add_fractions(1.5, 2, 1, 2)
        with self.assertRaises(TypeError):
            add_fractions(1, 2, "invalid", 2)
    
    def test_subtract_fractions(self):
        """Test fraction subtraction."""
        self.assertEqual(subtract_fractions(1, 2, 1, 3), (1, 6))
        self.assertEqual(subtract_fractions(3, 4, 1, 4), (1, 2))
        self.assertEqual(subtract_fractions(1, 2, 0, 1), (1, 2))
    
    def test_subtract_fractions_invalid(self):
        """Test fraction subtraction with invalid inputs."""
        with self.assertRaises(ValueError):
            subtract_fractions(1, 0, 1, 2)
        with self.assertRaises(ValueError):
            subtract_fractions(1, 2, 1, 0)
        with self.assertRaises(TypeError):
            subtract_fractions(1.5, 2, 1, 2)
        with self.assertRaises(TypeError):
            subtract_fractions(1, 2, "invalid", 2)
    
    def test_multiply_fractions(self):
        """Test fraction multiplication."""
        self.assertEqual(multiply_fractions(1, 2, 2, 3), (1, 3))
        self.assertEqual(multiply_fractions(3, 4, 4, 5), (3, 5))
        self.assertEqual(multiply_fractions(0, 1, 1, 2), (0, 1))
    
    def test_multiply_fractions_invalid(self):
        """Test fraction multiplication with invalid inputs."""
        with self.assertRaises(ValueError):
            multiply_fractions(1, 0, 1, 2)
        with self.assertRaises(ValueError):
            multiply_fractions(1, 2, 1, 0)
        with self.assertRaises(TypeError):
            multiply_fractions(1.5, 2, 1, 2)
        with self.assertRaises(TypeError):
            multiply_fractions(1, 2, "invalid", 2)
    
    def test_divide_fractions(self):
        """Test fraction division."""
        self.assertEqual(divide_fractions(1, 2, 2, 3), (3, 4))
        self.assertEqual(divide_fractions(3, 4, 1, 2), (3, 2))
        self.assertEqual(divide_fractions(1, 1, 1, 1), (1, 1))
    
    def test_divide_fractions_invalid(self):
        """Test fraction division with invalid inputs."""
        with self.assertRaises(ValueError):
            divide_fractions(1, 0, 1, 2)
        with self.assertRaises(ValueError):
            divide_fractions(1, 2, 1, 0)
        with self.assertRaises(ValueError):
            divide_fractions(1, 2, 0, 2)
        with self.assertRaises(TypeError):
            divide_fractions(1.5, 2, 1, 2)
        with self.assertRaises(TypeError):
            divide_fractions(1, 2, "invalid", 2)
    
    def test_decimal_to_fraction(self):
        """Test decimal to fraction conversion."""
        self.assertEqual(decimal_to_fraction(0.5), (1, 2))
        self.assertEqual(decimal_to_fraction(0.25), (1, 4))
        self.assertEqual(decimal_to_fraction(0.75), (3, 4))
        self.assertEqual(decimal_to_fraction(0), (0, 1))
        self.assertEqual(decimal_to_fraction(1), (1, 1))
        self.assertEqual(decimal_to_fraction(2), (2, 1))
    
    def test_decimal_to_fraction_invalid(self):
        """Test decimal to fraction conversion with invalid inputs."""
        with self.assertRaises(TypeError):
            decimal_to_fraction("invalid")

if __name__ == '__main__':
    unittest.main()