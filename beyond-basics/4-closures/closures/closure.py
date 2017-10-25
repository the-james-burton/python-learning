

def raise_to(exp):
    """
    This is a function factory, producing a
    function by (in this case) partially
    providing arguments to another function
    and returning that function.

    Functions are first class citizens

    see also functools.partial()
    """
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp
