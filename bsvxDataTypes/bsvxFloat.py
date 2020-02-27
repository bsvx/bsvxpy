#!/usr/bin/env python

from enum import Enum

class Precision(Enum):
    HALF = 0
    SINGLE = 1
    DOUBLE = 2
    TRIPLE = 3

class Float:
    def __init__(self, data, precision):
        # _data is integer
        self._data = self.set_data(data)
        # _precision is enum
        self._precision = self.set_precision(precision)

    def get_data(self):
        return self._data

    def get_precision(self):
        return self._precision

    def set_data(self, data):
        self._data = data

    def set_precision(self, precision):
        self._precision = precision
