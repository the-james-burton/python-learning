class SortedSet:

    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        return item in self._items
