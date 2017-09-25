#!/usr/bin/env python3
'''Deomstrate generators'''

import sys


def gen123():
    '''generators are iterators'''
    yield 1
    yield 2
    yield 3


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        seen.add(item)
        yield item



def main():
    # must get an instance first, since they are stateful...
    g = gen123()
    print(next(g))
    print(next(g))
    print(next(g))
    items = [2, 3, 3, 4, 4, 4, 5, 7, 7, 9]
    for item in distinct(items):
        print(item)


if __name__ == '__main__':
    main()
