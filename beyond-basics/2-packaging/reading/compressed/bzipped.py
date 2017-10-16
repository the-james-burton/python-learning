import bz2
import sys

opener = bz2.open

def bzip_file(file, text):
    f = bz2.open(file, mode='wt', encoding='utf-8')
    f.write(' '.join(text))
    f.close()

if __name__ == '__main__':
    bzip_file(sys.argv[1], sys.argv[2:])