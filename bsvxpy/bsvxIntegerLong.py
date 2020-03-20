#!/usr/bin/env python

from .bsvxIntegerShort import IntegerShort

class IntegerLong(IntegerShort):
    _long_length = None

    def __init__(self, input):
        mask = bytearray("07")
        self._long_length = int.from_bytes(input & mask) + 1

        self._length = int.from_bytes(self.read(None, self._long_length))
        #todo: zig-zag decoding of the 
        self._data = int.from_bytes(self.read(None, self._length))
