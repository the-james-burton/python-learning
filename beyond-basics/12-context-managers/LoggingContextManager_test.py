import unittest
from LoggingContextManager import *

class TestHandler(unittest.TestCase):

    def testLoggingContextManager(self):
        with LoggingContextManager() as cm:
            print(cm)