#!/usr/bin/env python3

from random import randrange


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


if __name__ == '__main__':
    main()
