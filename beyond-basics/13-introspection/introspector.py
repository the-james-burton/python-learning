import inspect
import reprlib
import itertools
import sorted_set


def print_table(rows_and_columns, *headers):
    pass

def full_sig(method):
    # easier to ask for forgiveness, than permission...
    try:
        return method.__name__ + str(inspect.signature(method))
    except ValueError:
        return method.__name__ + '(...)'

def brief_doc(obj):
    doc = obj.__doc__
    # look before you leap...
    if doc is not None:
        lines = doc.splitlines()
        if len(lines) > 0:
            # python convention is that the first line of the doc string
            # should contain a brief description, so we use it...
            return lines[0]
    return ''

def print_table(table, *headers):
    num_columns = len(table[0])
    num_headers = len(headers)
    if len(headers) != num_columns:
        raise TypeError("Expected {} header arguments, "
                        "got {}".format(num_columns, num_headers))
    table_with_header = itertools.chain([headers], table)
    columns_of_rows = list(zip(*table_with_header))
    column_widths = [max(map(len, column)) for column in columns_of_rows]
    # double curly braces to escape them...
    column_specs = ('{{:{w}}}'.format(w=width) for width in column_widths)
    format_spec = ' '.join(column_specs)
    print(format_spec.format(*headers))
    rules = ('-' * width for width in column_widths)
    print(format_spec.format(*rules))
    for row in table:
        print(format_spec.format(*row))

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
        filter(lambda attribute: callable(getattr(obj, attribute)),
        attributes))
    assert callables < attributes
    non_callables = attributes - callables
    attributes = [(name, reprlib.repr(getattr(obj, name)))
                             for name in attributes if "method-wrap" not in name[1]]
    print("*** ", attributes[0][1])
    attributes2 = list(itertools.filterfalse(lambda x: "method-wrap" in x[1], attributes))
    print_table(attributes2, "Name", "Value")

    print("Methods")
    print("=======")
    methods = (getattr(obj, method_name) for method_name in callables)
    methods = [(full_sig(method), brief_doc(method))
                            for method in methods]
    print_table(methods, "Name", "Description")


