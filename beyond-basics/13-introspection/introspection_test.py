import unittest

class TestHandler(unittest.TestCase):

    def testObjectIntrospection(self):
        i = 7
        # dir returns a list of attributes of an object...
        print(dir(i))
        # getattr returns the value of an attribute...
        print(getattr(i, 'denominator'))
        print(i.denominator)
        # attributes can also be methods...
        print(getattr(i, 'conjugate'))
        # callable returns true if the attribute is a method...
        print(callable(getattr(i, 'conjugate')))
        # we can get other properties...
        print(i.conjugate.__class__.__name__)
        # hasattr returns true if the object has the given attribute...
        print(hasattr(i, 'bit_length'))
        # testing for attributes is slower than handling exceptions
        # if the object does not have them

    def testScopeInstrospection(self):
        pass

    def testAttributeError(self):
        x = 5.6
        try:
            print(x.numerator)
        except AttributeError as e:
            print(x, "does not have numerator attribute")
