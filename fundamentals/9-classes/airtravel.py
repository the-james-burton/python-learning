'''airtravel'''


class Flight:
    # this is an init not a constructor, since the instance already exists when it is called...
    def __init__(self, number):
        # validations...
        if not number[:2].isalpha():
            raise ValueError("No airline code in:{}".format(number))
        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]


class Aircraft:
    def __init__(self, reg, model, rows, seats):
        self._reg = reg
        self._model = model
        self._rows = rows
        self._seats = seats

    def reg(self):
        return self._reg

    def model(self):
        return self._model