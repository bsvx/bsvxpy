#!/usr/bin/env python

from .bsvxIntegerShort import IntegerShort

class IntegerLong(IntegerShort):
    _long_length = None

    def __init__(self, input):
        mask = int('111', 2)
        self._long_length = (input & mask) + 1

        self._length = int(self.read(None, self._long_length), 16)
        #todo: zig-zag decoding
        self._data = int(self.read(None, self._length), 16)
