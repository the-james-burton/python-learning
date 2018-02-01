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

    def testAnnotatedCLoggingContextManagerWithException(self):
        with annotated_logging_context_manager() as cm:
            raise ValueError('I still hate you')

    def testNestedContextManagers(self):
        with annotated_logging_context_manager('inner1') as cm1, annotated_logging_context_manager('outer1') as cm2:
            print('cm1:{}, cm2:{}'.format(cm1, cm2))
        # eqivalent to...
        with annotated_logging_context_manager('inner2') as cm1:
            with annotated_logging_context_manager('outer2') as cm2:
                print('cm1:{}, cm2:{}'.format(cm1, cm2))
