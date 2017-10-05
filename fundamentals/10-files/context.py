#!/usr/bin/env python3
"""context"""

import sys
from itertools import islice
from pprint import pprint


def numbers():
    a, b = 0, 1
    while True:
        yield str(a)[0]
        a, b = b, a+b


def write_numbers(filename, count):
    f = open(filename, mode="wt", encoding="utf-8")
    f.writelines("{}\n".format(x) for x in islice(numbers(), count + 1))


def main():
    write_numbers("numbers.txt", 10)


if __name__ == '__main__':
    main()