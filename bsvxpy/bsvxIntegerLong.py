#!/usr/bin/env python

from .bsvxIntegerShort import IntegerShort

class IntegerLong(IntegerShort):

    def __init__(self, input):
        # Long int = 144 + [0,7]
        mask = int('111', 2)

        # long integers will use 1-8 bytes of data to represent its value
        # (input & mask) will map to integer values [0 - 7], + 1 to shift the range
        self._length = (input & mask) + 1

        #todo: zig-zag decoding
        self._data = int(self.read(None, self._length), 16)
