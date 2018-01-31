import unittest
from LoggingContextManager import *

class TestHandler(unittest.TestCase):

    def testLoggingContextManagerNoException(self):
        with LoggingContextManager() as cm:
            print(cm)

    def testLoggingContextManagerWithException(self):
        with LoggingContextManager() as cm:
            raise ValueError('I hate you')