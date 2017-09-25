#!/usr/bin/env python3
'''Deomstrate generators'''

import sys


def gen123():
    '''generators are iterators'''
    yield 1
    yield 2
    yield 3


def main():
    # must get an instance first, since they are stateful...
    g = gen123()
    print(next(g))
    print(next(g))
    print(next(g))


if __name__ == '__main__':
    main()
