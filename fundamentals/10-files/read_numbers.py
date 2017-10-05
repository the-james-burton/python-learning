#!/usr/bin/env python3
"""context"""

import sys
from itertools import islice
from pprint import pprint


def read_numbers_comprehension(filename):
    f = open(filename, mode="rt", encoding="utf-8")
    try:
        return [ int(line.strip()) for line in f]
    finally:
        f.close()



def read_numbers_simple(filename):
    f = open(filename, mode="rt", encoding="utf-8")
    try:
        numbers = []
        for line in f:
            x = int(line.strip())
            numbers.append(x)
    finally:
        f.close()
    return numbers


def print_numbers(filename):
    numbers = read_numbers_comprehension(filename);
    print(numbers)


def main():
    print_numbers("numbers.txt")


if __name__ == '__main__':
    main()