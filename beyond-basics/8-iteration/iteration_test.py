#!/usr/bin/env python3
"""shipping test"""

import unittest
from pprint import pprint

class IterationTest(unittest.TestCase):

    # def setUp(self):
    # def tearDown(self):

    def test_comprehension_equilavancy(self):
        values_from_comprehension = [x / (x - y) for x in range(10) if x > 5 for y in range(10) if x - y != 0]
        values_from_loop = []
        for x in range(10):
            if x > 5:
                for y in range(10):
                    if x - y != 0:
                        values_from_loop.append(x / (x - y))
        print(values_from_comprehension)
        print(values_from_loop)
        self.assertEqual(values_from_comprehension, values_from_loop)

    def test_nested_comprehensions(self):
        values_from_comprehension = [ [y * 3 for y in range(x)] for x in range(10)]
        values_from_loop = []
        for x in range(10):
            inner = []
            for y in range(x):
                inner.append(y * 3)
            values_from_loop.append(inner)
        print(values_from_comprehension)
        print(values_from_loop)
        self.assertEqual(values_from_comprehension, values_from_loop)


    def test_map(self):
        names = ['Alice', 'Bob', 'Chuck']
        result = map(lambda n : "Hello {}!".format(n), names)
        print(next(result))
        print(next(result))
        print(next(result))

if __name__  == '__main__':
    """run all tests in this module"""
    unittest.main()