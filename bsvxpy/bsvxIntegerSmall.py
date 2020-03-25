#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class IntegerSmall(bsvxDataType):
    # Small Int = 136 + [0, 7] : An integer in the range 0-7
    _mask = int('111', 2)

    def __init__(self, input):
        self._length = 0                # Small Int does not read data from file
        self._data = input & self._mask # data is the 0 - 7 value encoded in the input byte
        return