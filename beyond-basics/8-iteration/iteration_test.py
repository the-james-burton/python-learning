#!/usr/bin/env python3
"""shipping test"""

import unittest
from pprint import pprint

class IterationTest(unittest.TestCase):

    # def setUp(self):
    # def tearDown(self):

    def test_big_comprehension(self):
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

if __name__  == '__main__':
    """run all tests in this module"""
    unittest.main()