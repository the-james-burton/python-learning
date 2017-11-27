import bisect
from collections.abc import Sequence

class SortedSet(Sequence):
    """we inherit from Sequence to gain default implementations
    of index() and count(), see this page for more details
    https://docs.python.org/3.5/library/collections.abc.html"""

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

    def index(self, item):
        # improved performance version over the Sequence default implementation
        # This version is O(log n) instead of O(n) achieved by taking advantage
        # of the fact that each item can only appear once in the list, therefore
        # count can never be more than 1...
        index = bisect.bisect_left(self._items, item)
        if (index != len(self._items)) and (self._items[index] == item):
            return index
        raise ValueError("{} not found".format(repr(item)))


    def count(self, item):
        return int(item in self)