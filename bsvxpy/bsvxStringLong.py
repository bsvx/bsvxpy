#!/usr/bin/env python

from .bsvxStringShort import StringShort

class StringLong(StringShort):
    # Long String = 128 + [0,7] : 1-8 bytes giving the length of a UTF-8 encoded string, followed by said string
    _mask = int('111', 2)
    _long_length = None     # Intermediate variable used to store the length of the bytes that encode the length of the string

    def __init__(self, input):
        self._long_length = int(input, 16) & self._mask
        return

    # "Long" datatypes require a read operation to fetch 'length'
    def read_length(self, fileHandle):
        self._length = int(fileHandle.read(self._long_length), 16)
        return