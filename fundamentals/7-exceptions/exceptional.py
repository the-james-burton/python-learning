'''A module for demonstrating exceptions'''


def convert(s):
    try:
        x = int(s)
        print("success:", x)
    except ValueError:
        x = -1
        print("failed - {0} cannot be parsed as an int".format(s))
    except TypeError:
        x = -1
        print("failed - {0} is wrong type: {1}".format(s, type(s)))
    return x


def convert2(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return -1
