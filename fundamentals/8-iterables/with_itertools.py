#!/usr/bin/env python3
"""Demostrate itertools"""


import prime
from itertools import islice, count


def primes(y):
    return islice((x for x in count() if prime.is_prime(x)), y)


def main():
    print(list(primes(1000)))


if __name__ == '__main__':
    main()
