#!/usr/bin/env python3
"""Demonstrate modules"""

import os
import sys

from reading.compressed import *

# note the use of first class function references...
extension_map = {
    '.bz2': bz2_open,
    '.gz': gz_open
}

class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        # the 'open' here refers to the open function which will be used if
        # nothing is found in the map...
        opener = extension_map.get(extension, open)
        self.filename = filename
        self.f = opener(filename, 'rt', encoding='utf-8')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()

def main(filename):
    r = Reader(filename)
    print(r.read())

if __name__ == '__main__':
    main(sys.argv[1])