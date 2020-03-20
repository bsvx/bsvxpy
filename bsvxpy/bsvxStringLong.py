#!/usr/bin/env python

from bsvxpy import StringShort

class StringLong(StringShort):
    _long_length = None

    def __init__(self, input):
        mask = bytearray("07")
        self._long_length = int.from_bytes(input & mask)

        self._length = int.from_bytes(self.read(None, self._long_length))
        self._data = self.read(None, self._length).decode('utf-8')