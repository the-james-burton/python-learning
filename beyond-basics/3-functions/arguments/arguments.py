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

def print_args(arg, **kwargs):
    """**kwargs is presented to this function as a dictionary"""
    print(arg)
    print(type(kwargs))
    print(kwargs)

def tag(name, **attribs):
    result = ''
    for key, value in attribs.items():
        # this statement also uses keywords args...
        result += ' {k}="{v}"'.format(k=key, v=value)
    return '<{}{}>'.format(name, result)