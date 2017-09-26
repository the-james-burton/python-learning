#!/usr/bin/env python3
'''Deomstrate iterables'''

import sys
import math
import os
import glob
import prime
from pprint import pprint as pp


country_to_city = {'France': 'Paris',
                   'Russia': 'Moscow',
                   'Japan': 'Tokyo',
                   'India': 'Mubmai'}


weekdays = ['Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',]


def iterate_weekdays():
    iterable = iter(weekdays)
    try:
        while True:
            print(next(iterable))
    except StopIteration:
        print("end of iterable")


def list_comprehensions():
    return [len(str(math.factorial(x))) for x in range(20)]


def set_comprehensions():
    return {len(str(math.factorial(x))) for x in range(20)}


def city_to_country():
    return {city: country for country, city in country_to_city.items()}


def files_sizes(path):
    return {os.path.realpath(p): os.stat(p).st_size for p in glob.glob(path)}


def primes():
    return [x for x in range(101) if prime.is_prime(x)]


def prime_squares():
    return {x * x:(1, x, x * x) for x in range(101) if prime.is_prime(x)}


def main():
    print(list_comprehensions())
    print(set_comprehensions())
    print(country_to_city)
    print(city_to_country())
    pp(files_sizes('/usr/sbin/a*'))
    pp(primes())
    pp(prime_squares())
    iterate_weekdays()


if __name__ == '__main__':
    main()
