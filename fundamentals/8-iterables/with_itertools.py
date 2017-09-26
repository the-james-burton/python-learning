#!/usr/bin/env python3
"""Demostrate itertools"""


import prime
from itertools import islice, count, groupby, chain


def primes(y):
    return islice((x for x in count() if prime.is_prime(x)), y)


def describe(s):
    parsed = [ [ str(len(list(g))), k ] for k, g in groupby(s)]
    return "".join(list(chain.from_iterable(parsed)))


def main():
    print(list(primes(1000)))
    description = describe("1")
    for x in range(10):
        print(description)
        description = describe(description)


if __name__ == '__main__':
    main()
