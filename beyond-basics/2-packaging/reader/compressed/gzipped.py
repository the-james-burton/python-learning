import gzip
import sys

opener = gzip.open

def gzip_it(file):
    f = gzip.open(file, mode='wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()

if __name__ == '__main__':
    gzip_it(sys.argv[1])