from reading.compressed.gzipped import opener as gz_open
from reading.compressed.bzipped import opener as bz2_open

__all__ = ['gz_open', 'bz2_open']