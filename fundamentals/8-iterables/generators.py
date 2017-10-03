#!/usr/bin/env python3
"""Demostrate generators"""

import sys

def gen123():
    """generators are iterators"""
    yield 1
    yield 2
    yield 3


def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        seen.add(item)
        yield item


def sum_of_squares(y):
    # no parenthesis required for generator...
    return sum(x*x for x in range(1,y))


def main():
    # must get an instance first, since they are stateful...
    g = gen123()
    print(next(g))
    print(next(g))
    print(next(g))
    h = gen123()
    # note that generators complete normally when resolved fully...
    print(list(h))
    items = [2, 3, 3, 4, 4, 4, 5, 7, 7, 9]
    for item in take(3, distinct(items)):
        print(item)
    print(sum_of_squares(10000000))

if __name__ == '__main__':
    main()
