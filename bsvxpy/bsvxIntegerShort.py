#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class IntegerShort(bsvxDataType):
    def __init__(self, input):
        mask = int('111', 2)
        self._length = 0
        self._data = input & mask # data is the 0 - 7 value encoded in the original 
