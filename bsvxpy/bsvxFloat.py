#!/usr/bin/env python

from .bsvxDataType import bsvxDataType
from enum import Enum

class Precision(Enum):
    HALF = 0
    SINGLE = 1
    DOUBLE = 2

class Float(bsvxDataType):
    # Float = 152 + [0,7] : IEEE-754 format float. 1 = Single, 2 = Double
    _mask = int('111', 2)
    _precision = None       # Stores the float's precision. Preserves role of _length

    def __init__(self, input):
        self._precision = input & self._mask

        # Determines the Precision of the float       (E/M, bias)              Exponent bits / Significand bits
        # -----------------------------------------------------------------------------------------------------
        if self._precision == Precision.HALF:       # (5/11, exp. bias: 15)           0000 0 / 000 0000 0000
            self._length = 4
        elif self._precision == Precision.SINGLE:   # (8/24, exp. bias: 127)       0000 0000 / 0000 0000 0000 0000 0000 0000
            self._length = 8
        elif self._precision == Precision.DOUBLE:   # (11/53, exp. bias: 1023) 0000 0000 000 / 0 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
            self._length = 16

    # Helper Functions
    # ----------------
    # Should be called when writing to BSV OBJECT from a BSV FILE
    def decode(self, input): # returns a base 16 int with binary encoding
        #TODO convert input from zigzag encoding to binary encoding
        return input

    # Should be called when writing to BSV FILE from a BSV OBJECT
    def encode(self): # returns a base 16 int with zigzag encoding
        #TODO convert input from binary encoding to zigzag encoding
        return self._data


