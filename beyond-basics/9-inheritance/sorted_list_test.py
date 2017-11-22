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


    def test_int_list(self):
        il = sorted_list.IntList([4,2,7,5])
        pprint(il)
        il.add(1)
        pprint(il)
        with self.assertRaises(TypeError):
            il.add("banana")


    def test_sorted_int_list(self):
        sil = sorted_list.SortedIntList([6,2,8,4,9,1])
        pprint(sil)
        sil.add(7)
        pprint(sil)
        with self.assertRaises(TypeError):
            sil.add("banana")


    def test_super_proxy(self):
        pprint(sorted_list.SortedIntList.mro())
        validate = super(sorted_list.SortedIntList, sorted_list.SortedIntList)._validate
        print(validate(8))
        with self.assertRaises(TypeError):
            validate("banana")


    def test_instance_super_proxy(self):
        sil = sorted_list.SortedIntList([6,2,8,4,9,1])
        validate = super(sorted_list.SortedIntList, sil)._validate
        print(validate(8))
        with self.assertRaises(TypeError):
            validate("banana")


if __name__  == '__main__':
    """run all tests in this module"""
    unittest.main()