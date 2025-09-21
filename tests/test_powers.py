"""
Unit tests for the powers module.
"""

import unittest
import math
from src.calculator.modules.powers import *

class TestPowers(unittest.TestCase):
    """Test cases for power functions."""
    
    def test_power(self):
        """Test power function."""
        self.assertAlmostEqual(power(2, 3), 8, places=10)
        self.assertAlmostEqual(power(4, 0.5), 2, places=10)
        self.assertAlmostEqual(power(9, 0), 1, places=10)
        self.assertAlmostEqual(power(-2, 3), -8, places=10)
    
    def test_power_invalid(self):
        """Test power function with invalid inputs."""
        with self.assertRaises(ValueError):
            power(-2, 0.5)
        with self.assertRaises(TypeError):
            power("invalid", 2)
        with self.assertRaises(TypeError):
            power(2, "invalid")
    
    def test_sqrt(self):
        """Test square root function."""
        self.assertAlmostEqual(sqrt(4), 2, places=10)
        self.assertAlmostEqual(sqrt(0), 0, places=10)
        self.assertAlmostEqual(sqrt(2), math.sqrt(2), places=10)
    
    def test_sqrt_invalid(self):
        """Test square root function with invalid inputs."""
        with self.assertRaises(ValueError):
            sqrt(-1)
        with self.assertRaises(TypeError):
            sqrt("invalid")
    
    def test_cbrt(self):
        """Test cube root function."""
        self.assertAlmostEqual(cbrt(8), 2, places=10)
        self.assertAlmostEqual(cbrt(0), 0, places=10)
        self.assertAlmostEqual(cbrt(-8), -2, places=10)
        self.assertAlmostEqual(cbrt(27), 3, places=10)
    
    def test_cbrt_invalid(self):
        """Test cube root function with invalid inputs."""
        with self.assertRaises(TypeError):
            cbrt("invalid")
    
    def test_nth_root(self):
        """Test nth root function."""
        self.assertAlmostEqual(nth_root(8, 3), 2, places=10)
        self.assertAlmostEqual(nth_root(16, 4), 2, places=10)
        self.assertAlmostEqual(nth_root(0, 3), 0, places=10)
        self.assertAlmostEqual(nth_root(-8, 3), -2, places=10)
    
    def test_nth_root_invalid(self):
        """Test nth root function with invalid inputs."""
        with self.assertRaises(ValueError):
            nth_root(-4, 2)
        with self.assertRaises(ValueError):
            nth_root(4, -2)
        with self.assertRaises(ValueError):
            nth_root(4, 0)
        with self.assertRaises(ValueError):
            nth_root(4, 2.5)
        with self.assertRaises(TypeError):
            nth_root("invalid", 2)
        with self.assertRaises(TypeError):
            nth_root(4, "invalid")
    
    def test_exp(self):
        """Test exponential function."""
        self.assertAlmostEqual(exp(0), 1, places=10)
        self.assertAlmostEqual(exp(1), math.e, places=10)
        self.assertAlmostEqual(exp(2), math.e**2, places=10)
    
    def test_exp_invalid(self):
        """Test exponential function with invalid inputs."""
        with self.assertRaises(TypeError):
            exp("invalid")

    def test_square(self):
        """Test square function."""
        self.assertAlmostEqual(square(2), 4, places=10)
        self.assertAlmostEqual(square(0), 0, places=10)
        self.assertAlmostEqual(square(-3), 9, places=10)
        self.assertAlmostEqual(square(1.5), 2.25, places=10)
    
    def test_square_invalid(self):
        """Test square function with invalid inputs."""
        with self.assertRaises(TypeError):
            square("invalid")
    
    def test_cube(self):
        """Test cube function."""
        self.assertAlmostEqual(cube(2), 8, places=10)
        self.assertAlmostEqual(cube(0), 0, places=10)
        self.assertAlmostEqual(cube(-2), -8, places=10)
        self.assertAlmostEqual(cube(1.5), 3.375, places=10)
    
    def test_cube_invalid(self):
        """Test cube function with invalid inputs."""
        with self.assertRaises(TypeError):
            cube("invalid")

if __name__ == '__main__':
    unittest.main()