import datetime
import itertools
import random
import time

class Sensor:
    def __iter__(self):
        return self

    def __next__(self):
        return random.random()

