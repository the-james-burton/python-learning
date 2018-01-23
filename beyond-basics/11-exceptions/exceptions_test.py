import unittest
import sys
import exceptions
import io

class TestHandler(unittest.TestCase):

    def test_no_exception_given_integer(self):
        oldstdin = sys.stdin
        sys.stdin = io.StringIO('asdlkj')
        print(input())
        # handler.main()

    def test_demo_lookup_error(self):
        exceptions.demo_lookup_error()

    def test_median(self):
        print(exceptions.median([5,2,6,4,7,9]))
        try:
            exceptions.median([])
        # the function leaks implementation details and the exception is not very helpful...
        except ValueError as e:
            # only the left hand of the tuple is populated
            # so we could use e.args[0] instead...
            print("Payload:", e.args)
            print(str(e))