'''implementation of sqrt'''
from math import sqrt

def sqrth(x):
    '''Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root is to be computed.

    Returns:
        The square root of x.
    '''
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def compare(x):
    print("{} = math:{}, heron:{}".format(x, sqrt(x), sqrth(x)))


def main():
    compare(9)
    compare(2)
    try:
        print(sqrth(-1))
    except ZeroDivisionError:
        print("cannot compute square root of:{}".format(-1))

    print("carrying on...")

if __name__ == '__main__':
    main()