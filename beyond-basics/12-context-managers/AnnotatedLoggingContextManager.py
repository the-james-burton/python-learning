import contextlib
import sys


@contextlib.contextmanager
def annotated_logging_context_manager(name):
    print('LoggingContextManager.__enter__({})'.format(name))
    try:
        yield "{}: You're in a with-block!".format(name)
        print('LoggingContextManager.__exit__({})'.format(name))
    except Exception:
        print('LoggingContextManager.__exit__({}) [exception:{}]'
              .format(name, sys.exc_info()))
        # if you don't want to propagate the exception
        # don't call raise here...
        raise