class LoggingContextManager:

    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return "you are in a with-block"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('LoggingContextManager.__exit__() [type:{}, value:{}, traceback:{}]'
            .format(exc_type, exc_val, exc_tb))
        return