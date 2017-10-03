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


    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """Loop through all the seats and yield passengers one at a time"""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._bookings[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))


class Airplane:
    """effectively abstract, since it lacks a seating_plan() function"""
    def __init__(self, reg):
        self._reg = reg

    def reg(self):
        return self._reg

    def num_of_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)


class SmallAirplane(Airplane):
    def model(self):
        return "SmallAirplane"

    def seating_plan(self):
        return (range(1, 12), "ABCD")


class MediumAirplane(Airplane):
    def model(self):
        return "MediumAirplane"

    def seating_plan(self):
        return (range(1, 20), "ABCDEF")


def main():
    a = MediumAirplane("G-ABCD")
    print(a.reg())
    print(a.model())
    print(a.num_of_seats())
    pprint(a.seating_plan())

    f = Flight("NM064", SmallAirplane("G-WXYZ"))
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
    print(list(f._passenger_seats()))
    f.make_boarding_cards(console_card_printer)


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
             "  Flight: {1}" \
             "  Seat: {2}" \
             "  Aircraft: {3}" \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


if __name__ == '__main__':
    main()
