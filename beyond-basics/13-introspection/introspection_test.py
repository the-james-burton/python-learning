import unittest
from pprint import pprint

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
        # list all global attributes
        pprint(globals())
        # adding to and checking globals...
        globals()['a'] = 42
        print(globals()['a'])
        print('a' in globals())

        # adding to and checking locals...
        b = 24
        print(locals()['b'])
        print('b' in locals())
        # list all local attributes
        pprint(locals(), width=10)

        # selective printing of locals...
        fruit = 'apple'
        colour = 'green'
        taste = 'good'
        print("This {colour} {fruit} tastes {taste}".format(**locals()))

    def testAttributeError(self):
        x = 5.6
        try:
            print(x.numerator)
        except AttributeError as e:
            print(x, "does not have numerator attribute")
