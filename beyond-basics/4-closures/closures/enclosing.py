message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        global message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)

def get_message():
    return message