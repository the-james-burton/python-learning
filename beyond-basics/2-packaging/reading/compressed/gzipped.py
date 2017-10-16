import gzip
import sys

opener = gzip.open

def gzip_file(file, text):
    f = gzip.open(file, mode='wt', encoding='utf-8')
    f.write(' '.join(text))
    f.close()

if __name__ == '__main__':
    gzip_file(sys.argv[1], sys.argv[2:])