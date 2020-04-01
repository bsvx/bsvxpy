#!/usr/bin/env python

from .bsvxIntegerShort import IntegerShort

class IntegerLong(IntegerShort):
    # Long int = 144 + [0,7] : A zig-zag encoded integer using 1-8 bytes
    _mask = int('111', 2)

    def __init__(self, input):
        # A Long Integer uses 1-8 bytes of data to represent a value
        # (input & _mask) maps to integer values [0 - 7], + 1 to shift the range
        self._length = (input & self._mask) + 1
