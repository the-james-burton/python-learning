#!/usr/bin/env python3
"""sorted_list test"""

import unittest
import sorted_list
from pprint import pprint

class SortedListTest(unittest.TestCase):

    def test_sorted_list(self):
        sl = sorted_list.SortedList([6,2,8,4,9,1])
        pprint(sl)
        sl.add(7)
        pprint(sl)

if __name__  == '__main__':
    """run all tests in this module"""
    unittest.main()