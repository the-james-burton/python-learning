class LoggingContextManager:

    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return "you are in a with-block"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__()')
        else:
            print('LoggingContextManager.__exit__() [type:{}, value:{}, traceback:{}]'
            .format(exc_type, exc_val, exc_tb))
        # exceptions are propagated if the return value is false
        # since None = False, no return value will propagate exceptions
        # to swallow the exception, simply return True
        return