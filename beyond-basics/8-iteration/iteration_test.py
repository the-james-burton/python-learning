#!/usr/bin/env python3
"""shipping test"""

import unittest
import functools
import operator
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
        # note that map is lazy, so we wrap in list constructor to force evaluation...
        values_from_map = list(map(lambda n : "Hello {}!".format(n), names))
        values_from_comprehension = ["Hello {}!".format(n) for n in names]
        values_from_loop = []
        for n in names:
            values_from_loop.append("Hello {}!".format(n))
        print(values_from_map)
        print(values_from_comprehension)
        print(values_from_loop)
        self.assertEqual(values_from_map, values_from_comprehension)
        self.assertEqual(values_from_comprehension, values_from_loop)
        self.assertEqual(values_from_map, values_from_loop)

        surnames = ['Xavier', 'Yap', 'Zahn']
        # multiple inputs are sent to the mapping function as arguments...
        values_from_map = list(map(self.say_hello, names, surnames))
        print(values_from_map)


    def say_hello(self, name, surname):
        # multiple arguments to lambda are not supported,
        # so we declare a function
        return "Hello {} {}!".format(name, surname)


    def test_functools_reduce(self):
        values = [1,2,3,4,5,6,7,8,9]
        result = functools.reduce(self.show_add, values)
        pprint(result)


    def show_add(self, a, b):
        result = operator.add(a, b)
        print("add({},{}):{}".format(a, b, result))
        return result


if __name__  == '__main__':
    """run all tests in this module"""
    unittest.main()