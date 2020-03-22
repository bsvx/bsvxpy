#!/usr/bin/env python

from .bsvxStringShort import StringShort

class StringLong(StringShort):
    _long_length = None

    def __init__(self, input):
        mask = int('111', 2)
        self._long_length = input & mask

        self._length = int(self.read(None, self._long_length), 16)
        self._data = self.read(None, self._length).decode('utf-8')