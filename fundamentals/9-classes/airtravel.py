#!/usr/bin/env python3
"""airtravel"""
from pprint import pprint


class Flight:
    """A flight on a given aircraft"""

    # this is an init not a constructor, since the instance already exists when it is called...
    def __init__(self, number, aircraft):
        # validations...
        if not number[:2].isalpha():
            raise ValueError("No airline code in:{}".format(number))

        self._number = number
        self._aircraft = aircraft

        # unpack the single tuple returned by seating_plan()
        # which is a range of the number of rows and an int of seats per row...
        rows, seats = self._aircraft.seating_plan()

        # initialize a booking grid for the seating plan
        # this will be a list of dictionaries per row...
        self._bookings = [None] + [ {s:None for s in seats} for _ in rows ]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def bookings(self):
        return self._bookings

    def available_seats(self):
        return sum( sum (1 for seat in row.values() if seat is None) for row in self._bookings if row is not None )

    def _parse_seat(self, seat):
        # get the aircraft seating plan so we can validate against it...
        rows, seats = self._aircraft.seating_plan()

        # get the last character of the given seat string, which should be a letter...
        # (use negative indexing to get the last character)
        letter = seat[-1]

        # is the letter on the plan?
        if letter not in seats:
            raise ValueError("Invalid seat letter:{}".format(letter))

        # is the row an integer?
        try:
            # (get the row number by using string slicing to get all but the last character)
            row_text = seat[:-1]
            row = int(row_text)
        except:
            raise ValueError("Row must be an integer:{}".format(row_text))

        # is the given row on the plan?
        if row not in rows:
            raise ValueError("Invalid row number:{}".format(row))

        return row, letter

    def book(self, seat, passenger):
        """Book the given passenger into the given seat
        Args:
            seat: seat in concatenated row, seat format, e.g. '6B',
            passenger: string of passenger name, e.g. 'John Smith'

        Raises:
            ValueError: if seat is already taken
        """
        row, letter = self._parse_seat(seat)

        # is the seat already taken?
        if self._bookings[row][letter] is not None:
            raise ValueError("Seat is already taken:{}".format(seat))

        # all good, so book the seat...
        self._bookings[row][letter] = passenger
        print("{} booked into seat {}{}".format(passenger, row, letter))

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
    print(f.bookings())
    try:
        f.book("48A", "Anthony Zebra")
    except ValueError as e:
        print(e)
    try:
        f.book("48Z", "Anthony Zebra")
    except ValueError as e:
        print(e)
    print(f.available_seats())
    try:
        f.book("2B", "Zoltan Armadillo")
        f.book("3B", "Yves Bear")
        f.book("2C", "Xander Crow")
        f.book("2B", "Will Dear")
    except ValueError as e:
        print(e)
    pprint(f.bookings())
    print(f.available_seats())

if __name__ == '__main__':
    main()
