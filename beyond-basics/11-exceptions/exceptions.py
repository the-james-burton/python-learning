#!/usr/bin/env python3

from random import randrange

import math


def main():
    number = randrange(10)
    while True:
        try:
            guess = int(input("? "))
        # ALWAYS specify an exception type...
        except ValueError:
            continue
        if guess == number:
            print("You win!")
            break

def demo_lookup_error():
    s = [1, 4, 6]
    try:
        item = s[5]
    # IndexError inherits from LookupError
    except LookupError:
        print("Handled IndexError")

    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    # KeyError also inherits from LookupError
    except LookupError:
        print("Handled KeyError")

def median(iterable):
    """Obtain the central value of a series.

    Sorts the iterable and returns the middle value if there is an even
    number of elements, or the arithmetic mean of the middle two elements
    if there is an even number of elements.

    Args:
        iterable: A series of orderable items.

    Returns:
        The median value.
    """
    items = sorted(iterable)
    median_index = (len(items) - 1) // 2
    if len(items) == 0:
        raise ValueError("arg is an empty sequence")
    if len(items) % 2 != 0:
        return items[median_index]
    return (items[median_index] + items[median_index + 1]) / 2.0

def demo_unicode_error():
    b'hello\x81world'.decode('utf-8')


class TriangleError(Exception):
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)

    def __repr__(self):
        return "TriangleError({!r}, {!r}".format(self.args[0], self._sides)


def triangle_area(a, b, c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle", sides)
    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e


if __name__ == '__main__':
    main()
