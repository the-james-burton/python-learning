#!/usr/bin/env python3
"""functions to demonstrate extended arguments"""

def hypervolume(*lengths):
    """will raise a unwanted StopIteration if no lengths"""
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

def hypervolume2(first_length, *next_lengths):
    """although there are two parameters, this does not
    change the interface for callers"""
    v = first_length
    for l in next_lengths:
        v *= l
    return v

def print_kwargs(arg, **kwargs):
    """**kwargs is presented to this function as a dictionary"""
    print(arg)
    print(type(kwargs))
    print(kwargs)

def print_args(arg1, arg2, *args):
    """**kwargs is presented to this function as a dictionary"""
    print(arg1)
    print(arg2)
    print(args)

def tag(name, **attribs):
    result = ''
    for key, value in attribs.items():
        # this statement also uses keywords args...
        result += ' {k}="{v}"'.format(k=key, v=value)
    return '<{}{}>'.format(name, result)

def colour(red, green, blue, **kwargs):
    print("r = ", red)
    print("g = ", green)
    print("b = ", blue)
    print(kwargs)
