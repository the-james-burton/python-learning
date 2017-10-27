# ========================================
# functions as decorators
# ========================================
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


# ========================================
# classes as decorators
# ========================================
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


# ========================================
# instances as decorators
# ========================================
class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            result = f(*args, **kwargs)
            if self.enabled:
                print('Called {}'.format(f))
            return result
        return wrap

# this is the difference here
# see that an instance name is used
# as decorator and not the class name
tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]