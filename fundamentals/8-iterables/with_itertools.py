#!/usr/bin/env python3
"""Demostrate itertools"""


import prime
from itertools import islice, count, groupby, chain
from statistics import mean

saturday = [3,3,4,6,8,9,8,6,5,4,3,3]
sunday   = [4,4,5,6,8,8,9,9,7,6,6,6]


def zip_avg(a,b):
    for x in zip(a, b):
        print(mean(x))


def primes(y):
    return islice((x for x in count() if prime.is_prime(x)), y)


def describe(s):
    parsed = [ [ str(len(list(g))), k ] for k, g in groupby(s)]
    return "".join(list(chain.from_iterable(parsed)))


def main():
    print(list(primes(100)))
    print(list(zip(saturday, sunday)))
    zip_avg(saturday, sunday)
    description = describe("1")
    for x in range(10):
        print(description)
        description = describe(description)


if __name__ == '__main__':
    main()
