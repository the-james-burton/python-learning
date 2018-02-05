import inspect
import reprlib

import sorted_set


def print_table(rows_and_columns, *headers):
    pass


def full_sig(method):
    pass


def brief_doc(obj):
    pass


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
    ## getmembers will work just fine for this,
    # but we do it from first principles here...
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
    methods = (getattr(obj, method_name) for method_name in callables)
    methods = [(full_sig(method), brief_doc(method))
                            for method in methods]
    print_table(methods, "Name", "Description")


