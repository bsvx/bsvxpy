#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class Blob(bsvxDataType):
    # Blob = 160 + [0,7] : 1 - 8 bytes giving the length of binary data in bytes, followed by that data
    _mask = int('111', 2)
    _long_length = None     # Intermediate variable used to store the length of the bytes that encode the length of the Blob

    def __init__(self, input):
        # A Blob uses 1-8 bytes of data to represent a value
        # (input & _mask) maps to integer values [0 - 7], + 1 to shift the range
        bsvxDataType.__init__(self, input)
        self._long_length = (int(input, 16) & self._mask) + 1
        return

    # Accessor Functions
    # ------------------
    # "Long" datatypes require a read operation to fetch 'length'
    def read_length(self, fileHandle):
        self._length = int(fileHandle.read(self._long_length), 16)
        return