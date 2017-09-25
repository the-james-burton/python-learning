#!/usr/bin/env python3
'''Deomstrate iterables'''

import sys
import math
import os
import glob
from pprint import pprint as pp

country_to_city = {'France': 'Paris',
                   'Russia': 'Moscow',
                   'Japan': 'Tokyo',
                   'India': 'Mubmai'}


def list_comprehensions():
    return [len(str(math.factorial(x))) for x in range(20)]


def set_comprehensions():
    return {len(str(math.factorial(x))) for x in range(20)}


def city_to_country():
    return {city: country for country, city in country_to_city.items()}


def files_sizes(path):
    return {os.path.realpath(p): os.stat(p).st_size for p in glob.glob(path)}


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes():
    return [x for x in range(101) if is_prime(x)]


def main():
    print(list_comprehensions())
    print(set_comprehensions())
    print(country_to_city)
    print(city_to_country())
    pp(files_sizes('/usr/sbin/a*'))
    pp(primes())

if __name__ == '__main__':
    main()
