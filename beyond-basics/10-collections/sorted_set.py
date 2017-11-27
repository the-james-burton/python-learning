class SortedSet:

    def __init__(self, items=None):
        """if no starting list is given, then initialize
            with a new empty list"""
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        """implements the container protocol"""
        return item in self._items

    def __len__(self):
        """implements the sized protocol"""
        return len(self._items)