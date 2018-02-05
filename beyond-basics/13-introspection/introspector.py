import inspect
import reprlib

import sorted_set


def dump(obj):
    print("Type")
    print("====")
    print(type(obj))
    print()

    print("Documentation")
    print("=============")
    print(inspect.getdoc(obj))

    print("Attributes")
    print("==========")
    attributes = sorted_set.SortedSet(dir(obj))
    callables = sorted_set.SortedSet(
        filter(lambda attribute: callable(obj, getattr(obj, attribute))),
        attributes
    )
    assert callables < attributes
    non_callables = attributes - callables
    attributes = [(name, reprlib.repr(getattr(obj, name)))
                             for name in attributes]
    print_table(attributes, "Name", "Value")

    print("Methods")
    print("=======")
    # TODO


