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

    def test_demo_unicode_error(self):
        try:
            exceptions.demo_unicode_error()
        # note how UnicodeError has additional properties...
        except UnicodeError as e:
            print(e)
            print("encoding:", e.encoding)
            print("reason:", e.reason)
            print("object:", e.object)
            print("start:", e.start)
            print("end", e.end)

    def test_triangle_error(self):
        print("area:{0}".format(str(exceptions.triangle_area(3,4,5))))
        print("area:{0}".format(str(exceptions.triangle_area(3,4,10))))


