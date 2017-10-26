message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        # use 'global' to bring a global variable into this scope...
        # global message
        # use 'nonlocal' to bring the variable in the next
        # wider scope into this scope...
        nonlocal message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)

def get_message():
    return message