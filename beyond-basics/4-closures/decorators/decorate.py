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