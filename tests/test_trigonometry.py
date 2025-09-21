"""
Unit tests for the trigonometry module.
"""

import unittest
import math
from src.calculator.modules.trigonometry import *

class TestTrigonometry(unittest.TestCase):
    """Test cases for trigonometry functions."""
    
    def test_sin_radians(self):
        """Test sine function with radians."""
        self.assertAlmostEqual(sin(0), 0, places=10)
        self.assertAlmostEqual(sin(math.pi/2), 1, places=10)
        self.assertAlmostEqual(sin(math.pi), 0, places=10)
        self.assertAlmostEqual(sin(3*math.pi/2), -1, places=10)
    
    def test_sin_degrees(self):
        """Test sine function with degrees."""
        self.assertAlmostEqual(sin(0, degrees=True), 0, places=10)
        self.assertAlmostEqual(sin(90, degrees=True), 1, places=10)
        self.assertAlmostEqual(sin(180, degrees=True), 0, places=10)
        self.assertAlmostEqual(sin(270, degrees=True), -1, places=10)
    
    def test_cos_radians(self):
        """Test cosine function with radians."""
        self.assertAlmostEqual(cos(0), 1, places=10)
        self.assertAlmostEqual(cos(math.pi/2), 0, places=10)
        self.assertAlmostEqual(cos(math.pi), -1, places=10)
        self.assertAlmostEqual(cos(3*math.pi/2), 0, places=10)
    
    def test_cos_degrees(self):
        """Test cosine function with degrees."""
        self.assertAlmostEqual(cos(0, degrees=True), 1, places=10)
        self.assertAlmostEqual(cos(90, degrees=True), 0, places=10)
        self.assertAlmostEqual(cos(180, degrees=True), -1, places=10)
        self.assertAlmostEqual(cos(270, degrees=True), 0, places=10)
    
    def test_tan_radians(self):
        """Test tangent function with radians."""
        self.assertAlmostEqual(tan(0), 0, places=10)
        self.assertAlmostEqual(tan(math.pi/4), 1, places=10)
        self.assertAlmostEqual(tan(3*math.pi/4), -1, places=10)
    
    def test_tan_degrees(self):
        """Test tangent function with degrees."""
        self.assertAlmostEqual(tan(0, degrees=True), 0, places=10)
        self.assertAlmostEqual(tan(45, degrees=True), 1, places=10)
        self.assertAlmostEqual(tan(135, degrees=True), -1, places=10)
    
    def test_tan_undefined(self):
        """Test tangent function with undefined values."""
        with self.assertRaises(ValueError):
            tan(math.pi/2)
        with self.assertRaises(ValueError):
            tan(90, degrees=True)
    
    def test_asin(self):
        """Test arc sine function."""
        self.assertAlmostEqual(asin(0), 0, places=10)
        self.assertAlmostEqual(asin(1), math.pi/2, places=10)
        self.assertAlmostEqual(asin(-1), -math.pi/2, places=10)
    
    def test_asin_invalid(self):
        """Test arc sine function with invalid inputs."""
        with self.assertRaises(ValueError):
            asin(2)
        with self.assertRaises(ValueError):
            asin(-2)
    
    def test_acos(self):
        """Test arc cosine function."""
        self.assertAlmostEqual(acos(1), 0, places=10)
        self.assertAlmostEqual(acos(0), math.pi/2, places=10)
        self.assertAlmostEqual(acos(-1), math.pi, places=10)
    
    def test_acos_invalid(self):
        """Test arc cosine function with invalid inputs."""
        with self.assertRaises(ValueError):
            acos(2)
        with self.assertRaises(ValueError):
            acos(-2)
    
    def test_atan(self):
        """Test arc tangent function."""
        self.assertAlmostEqual(atan(0), 0, places=10)
        self.assertAlmostEqual(atan(1), math.pi/4, places=10)
        self.assertAlmostEqual(atan(-1), -math.pi/4, places=10)
    
    def test_sinh(self):
        """Test hyperbolic sine function."""
        self.assertAlmostEqual(sinh(0), 0, places=10)
        self.assertAlmostEqual(sinh(1), (math.e - 1/math.e)/2, places=10)
    
    def test_cosh(self):
        """Test hyperbolic cosine function."""
        self.assertAlmostEqual(cosh(0), 1, places=10)
        self.assertAlmostEqual(cosh(1), (math.e + 1/math.e)/2, places=10)
    
    def test_tanh(self):
        """Test hyperbolic tangent function."""
        self.assertAlmostEqual(tanh(0), 0, places=10)
        self.assertAlmostEqual(tanh(1), sinh(1)/cosh(1), places=10)
    
    def test_invalid_inputs(self):
        """Test functions with invalid input types."""
        with self.assertRaises(TypeError):
            sin("invalid")
        with self.assertRaises(TypeError):
            cos("invalid")
        with self.assertRaises(TypeError):
            tan("invalid")
        with self.assertRaises(TypeError):
            asin("invalid")
        with self.assertRaises(TypeError):
            acos("invalid")
        with self.assertRaises(TypeError):
            atan("invalid")
        with self.assertRaises(TypeError):
            sinh("invalid")
        with self.assertRaises(TypeError):
            cosh("invalid")
        with self.assertRaises(TypeError):
            tanh("invalid")

if __name__ == '__main__':
    unittest.main()