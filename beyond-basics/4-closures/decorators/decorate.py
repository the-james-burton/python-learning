def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap

city = 'Tromsø'

def get_city():
    return city

# the '@' symbol here will pass the result of the 'get_city2'
# function through the 'escape_unicode' function before returning it...
@escape_unicode
def get_city2():
    return city


class CallCount:
    def __init__(self, f):
        self.f = f
        # this property will be visible when a function is decorated
        # with this class...
        self.count = 0

    def __call__(self, *args, **kwargs):
        """ classes MUST implement this method
        to be used as a decorator"""
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('Hello, {}'.format(name))

