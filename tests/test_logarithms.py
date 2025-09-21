"""
Unit tests for the logarithms module.
"""

import unittest
import math
from src.calculator.modules.logarithms import *

class TestLogarithms(unittest.TestCase):
    """Test cases for logarithm functions."""
    
    def test_ln(self):
        """Test natural logarithm function."""
        self.assertAlmostEqual(ln(1), 0, places=10)
        self.assertAlmostEqual(ln(math.e), 1, places=10)
        self.assertAlmostEqual(ln(math.e**2), 2, places=10)
    
    def test_ln_invalid(self):
        """Test natural logarithm function with invalid inputs."""
        with self.assertRaises(ValueError):
            ln(0)
        with self.assertRaises(ValueError):
            ln(-1)
        with self.assertRaises(TypeError):
            ln("invalid")
    
    def test_log10(self):
        """Test logarithm base 10 function."""
        self.assertAlmostEqual(log10(1), 0, places=10)
        self.assertAlmostEqual(log10(10), 1, places=10)
        self.assertAlmostEqual(log10(100), 2, places=10)
    
    def test_log10_invalid(self):
        """Test logarithm base 10 function with invalid inputs."""
        with self.assertRaises(ValueError):
            log10(0)
        with self.assertRaises(ValueError):
            log10(-1)
        with self.assertRaises(TypeError):
            log10("invalid")
    
    def test_log2(self):
        """Test logarithm base 2 function."""
        self.assertAlmostEqual(log2(1), 0, places=10)
        self.assertAlmostEqual(log2(2), 1, places=10)
        self.assertAlmostEqual(log2(4), 2, places=10)
        self.assertAlmostEqual(log2(8), 3, places=10)
    
    def test_log2_invalid(self):
        """Test logarithm base 2 function with invalid inputs."""
        with self.assertRaises(ValueError):
            log2(0)
        with self.assertRaises(ValueError):
            log2(-1)
        with self.assertRaises(TypeError):
            log2("invalid")
    
    def test_log(self):
        """Test general logarithm function."""
        self.assertAlmostEqual(log(1), 0, places=10)
        self.assertAlmostEqual(log(math.e), 1, places=10)
        self.assertAlmostEqual(log(8, 2), 3, places=10)
        self.assertAlmostEqual(log(10, 10), 1, places=10)
    
    def test_log_invalid(self):
        """Test general logarithm function with invalid inputs."""
        with self.assertRaises(ValueError):
            log(0)
        with self.assertRaises(ValueError):
            log(-1)
        with self.assertRaises(ValueError):
            log(10, 0)
        with self.assertRaises(ValueError):
            log(10, -1)
        with self.assertRaises(ValueError):
            log(10, 1)
        with self.assertRaises(TypeError):
            log("invalid")
        with self.assertRaises(TypeError):
            log(10, "invalid")

if __name__ == '__main__':
    unittest.main()