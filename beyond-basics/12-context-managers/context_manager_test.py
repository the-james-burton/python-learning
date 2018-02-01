import unittest
from LoggingContextManager import *
from AnnotatedLoggingContextManager import *

class TestHandler(unittest.TestCase):

    def testLoggingContextManagerNoException(self):
        with LoggingContextManager() as cm:
            print(cm)

    def testLoggingContextManagerWithException(self):
        with LoggingContextManager() as cm:
            raise ValueError('I hate you')

    def testAnnotatedCLoggingContextManager(self):
        with annotated_logging_context_manager() as cm:
            print(cm)