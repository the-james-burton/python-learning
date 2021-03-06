import bisect
from collections.abc import Sequence, Set
from itertools import chain


class SortedSet(Sequence, Set):
    """
    There is no longer any strict need to inherit from
    Sequence. We have now implemented improved versions of
    index() and count(). However, the issubclass() method
    will return True if we do inherit from Sequence
    making it more obvious what this class is.

    we previously inherited from Sequence to gain default
    implementations of index() and count(), see this page for
    more details
    https://docs.python.org/3.5/library/collections.abc.html

    This is an immutable collection.

    For a mutable set, inherit MutableSet and implement
    add(), discard(), update(), plus any others.
    """

    def __init__(self, items=None):
        """if no starting list is given, then initialize
            with a new empty list"""
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        """implements the container protocol"""
        # return item in self._items
        # leverage improved performance index() function
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        """implements the sized protocol"""
        return len(self._items)

    def __iter__(self):
        """implements the iterable protocol"""
        return iter(self._items)
        # to use a generator, it would look like this...
        # for item in self._items: yield item

    def __getitem__(self, index):
        """implements the iterable protocol"""
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        """implements the repr protocol"""
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self, other):
        if not isinstance(other, SortedSet):
            # note that we don't raise the exception ourselves
            # since python will raise it for us...
            return NotImplemented
        return self._items == other._items

    def __ne__(self, other):
        if not isinstance(other, SortedSet):
            # the docs say we need to implement this...
            return NotImplemented
        return self._items != other._items

    def _is_unique_and_sorted(self):
        return all(self[i] < self[i + 1] for i in range(len(self) - 1))

    def index(self, item):
        # make an assertion...
        assert(self._is_unique_and_sorted())
        # improved performance version over the Sequence default implementation
        # This version is O(log n) instead of O(n) achieved by taking advantage
        # of the fact that each item can only appear once in the list, therefore
        # count can never be more than 1...
        index = bisect.bisect_left(self._items, item)
        if (index != len(self._items)) and (self._items[index] == item):
            return index
        raise ValueError("{} not found".format(repr(item)))

    def count(self, item):
        assert(self._is_unique_and_sorted())
        return int(item in self)

    def __add__(self, other):
        return SortedSet(chain(self._items, other._items))

    def __mul__(self, times):
        return self if times > 0 else SortedSet()

    def __rmul__(self, times):
        return self * times;

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)

