import contextlib
import sys


@contextlib.contextmanager
def annotated_logging_context_manager():
    print('LoggingContextManager.__enter__()')
    try:
        yield "You're in a with-block!"
        print('LoggingContextManager.__exit__()')
    except Exception:
        print('LoggingContextManager.__exit__() [exception:{}]'
              .format(sys.exc_info()))
        # if you don't want to propagate the exception
        # don't call raise here...
        raise