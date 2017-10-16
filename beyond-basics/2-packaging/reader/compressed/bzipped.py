import bz2
import sys

opener = bz2.open

def bzip_it(file):
    f = bz2.open(file, mode='wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()

if __name__ == '__main__':
    bzip_it(sys.argv[1])