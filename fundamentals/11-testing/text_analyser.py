#!/usr/bin/env python3
"""testing"""

import os
import unittest

def analyse_text(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = 0
        chars = 0
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)

class TextAnalyserTest(unittest.TestCase):

    def setUp(self):
        """this function is a 'fixture' which sets up initial conditions for the tests
            runs before every test function"""
        ipsum = ("Illum quidem fuga voluptatem atque.\n"
                 "Incidunt magnam alias ad at ut et est et.\n"
                 "Repudiandae voluptatem quisquam est. A voluptatem vel modi.\n"
                 "Officia aut laborum non voluptates dolor ex error.")
        self.filename = 'test_file.txt'
        with open(self.filename, mode='w', encoding='utf-8') as f:
            f.write(ipsum)

    def tearDown(self):
        """this function is a 'fixture' which removes the initial conditions for the tests
            runs after every test method"""
        try:
            os.remove(self.filename)
        except:
            pass

    # prefixing a method with 'test_' is required for automatic execution...
    def test_function_runs(self):
        analyse_text(self.filename)

    def test_line_count(self):
        actual = analyse_text(self.filename)[0]
        self.assertEqual(actual, 4)

    def test_character_count(self):
        actual = analyse_text(self.filename)[1]
        self.assertEqual(actual, 188)

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyse_text("does_not_exist.txt")

    def test_does_not_delete(self):
        analyse_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__  == '__main__':
    """run all tests in this module"""
    unittest.main()