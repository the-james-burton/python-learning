#!/usr/bin/env python3
"""airtravel"""


class Flight:
    """A flight on a given aircraft"""

    # this is an init not a constructor, since the instance already exists when it is called...
    def __init__(self, number, aircraft):
        # validations...
        if not number[:2].isalpha():
            raise ValueError("No airline code in:{}".format(number))

        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()


class Aircraft:
    def __init__(self, reg, model, rows, seats_per_row):
        self._reg = reg
        self._model = model
        self._rows = rows
        self._seats_per_row = seats_per_row

    def reg(self):
        return self._reg

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._rows + 1), "ABCDEFGHJK"[:self._seats_per_row])


def main():
    a = Aircraft("G-ABCD", "Small plane of some sort", rows=8, seats_per_row=3)
    print(a.reg())
    print(a.model())
    print(a.seating_plan())

    f = Flight("NM064", Aircraft("G-WXYZ", "Slightly bigger plane", rows=10, seats_per_row=4))
    print(f.aircraft_model())

if __name__ == '__main__':
    main()
