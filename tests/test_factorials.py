"""
Unit tests for the factorials module.
"""

import unittest
import math
from src.calculator.modules.factorials import *

class TestFactorials(unittest.TestCase):
    """Test cases for factorial functions."""
    
    def test_factorial(self):
        """Test factorial function."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
    
    def test_factorial_invalid(self):
        """Test factorial function with invalid inputs."""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial("invalid")
    
    def test_double_factorial(self):
        """Test double factorial function."""
        self.assertEqual(double_factorial(0), 1)
        self.assertEqual(double_factorial(1), 1)
        self.assertEqual(double_factorial(5), 15)  # 5 * 3 * 1
        self.assertEqual(double_factorial(6), 48)  # 6 * 4 * 2
        self.assertEqual(double_factorial(8), 384)  # 8 * 6 * 4 * 2
    
    def test_double_factorial_invalid(self):
        """Test double factorial function with invalid inputs."""
        with self.assertRaises(ValueError):
            double_factorial(-1)
        with self.assertRaises(TypeError):
            double_factorial(3.5)
        with self.assertRaises(TypeError):
            double_factorial("invalid")
    
    def test_gamma(self):
        """Test gamma function."""
        self.assertAlmostEqual(gamma(1), 1, places=10)
        self.assertAlmostEqual(gamma(2), 1, places=10)
        self.assertAlmostEqual(gamma(3), 2, places=10)
        self.assertAlmostEqual(gamma(4), 6, places=10)
        self.assertAlmostEqual(gamma(0.5), math.sqrt(math.pi), places=10)
    
    def test_gamma_invalid(self):
        """Test gamma function with invalid inputs."""
        with self.assertRaises(ValueError):
            gamma(0)
        with self.assertRaises(ValueError):
            gamma(-1)
        with self.assertRaises(ValueError):
            gamma(-2)
        with self.assertRaises(TypeError):
            gamma("invalid")

if __name__ == '__main__':
    unittest.main()