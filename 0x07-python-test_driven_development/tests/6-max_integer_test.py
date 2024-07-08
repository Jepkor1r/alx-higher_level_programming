#!/usr/bin/python3
"""
   
    Unittest for max_integer

"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([9, 1, 5]), 9)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_negative(self):
        self.assertEqual(max_integer([-9, -1, -5]), -1)

    def test_float_numbers(self):
        self.assertEqual(max_integer([3.5, 2.1, 4.6]), 4.6)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([3, 2.1, 4]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_strings(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])

    def test_non_iterable(self):
        with self.assertRaises(TypeError):
            max_integer(123)

if __name__ == "__main__":
    unittest.main()
