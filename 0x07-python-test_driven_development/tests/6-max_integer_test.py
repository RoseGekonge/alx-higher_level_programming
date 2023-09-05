#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_value(self):
        self.assertAlmostEqual(max_integer([1, 3, 4, 2, 7]), 7)
        self.assertAlmostEqual(max_integer([1, 3, 4, 23, 2]), 23)
        self.assertAlmostEqual(max_integer([]), None)
