#!/usr/bin/env python

from .bsvxDataType import bsvxDataType
from .bsvxStringShort import StringShort

class StringLong(StringShort):
    # Long String = 128 + [0,7] : 1-8 bytes giving the length of a UTF-8 encoded string, followed by said string
    _mask = int('111', 2)
    _long_length = None     # Intermediate variable used to store the length of the bytes that encode the length of the string
    _long_type = True

    def __init__(self, input):
        bsvxDataType.__init__(self, input)

        if type(input) is int:                              # REGULAR STRING INPUT
            self._data = input
            self._hex_data = hex(input).lstrip('0x')
            self._length = len(self._hex_data) / 2
        else:                                               # HEX BYTE FOR READING FROM FILE
            self._long_length = (int(input, 16) & self._mask) + 1

    # "Long" datatypes require a read operation to fetch 'length'
    def read_length(self, fileHandle):
        self._length = int(fileHandle.read(self._long_length * 2), 16)
        return

    def set_data(self, data=None):
        self.from_binary_encoding(data)
        return