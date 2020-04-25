#!/usr/bin/env python

from .bsvxHeader import Header

class HeaderLong(Header):
    # Long Header = 184 + [0,7] : 1-8 bytes giving the number of fields in the Header
    _mask = int('111', 2)
    _long_length = None     # Intermediate variable used to store the length of the bytes that encode the length of the 'field_count'

    def __init__(self, input):
        bsvxDataType.__init__(self, input)
        # A Long Header uses 1-8 bytes of data to represent its 'field_count'
        # (input & _mask) maps to integer values [0 - 7], + 1 to shift the range
        self._long_length = (int(input, 16) & self._mask) + 1
        return

    # Helper Functions
    # ----------------
    # "Long" datatypes require a read operation to fetch 'length'
    def read_length(self, fileHandle):
        self._length = int(fileHandle.read(self._long_length), 16)
        return