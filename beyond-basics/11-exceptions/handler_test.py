import unittest
import sys
import handler
import io

class TestHandler(unittest.TestCase):

    def test_no_exception_given_integer(self):
        oldstdin = sys.stdin
        sys.stdin = io.StringIO('asdlkj')
        print(input())
        # handler.main()

    def test_demo_lookup_error(self):
        handler.demo_lookup_error()