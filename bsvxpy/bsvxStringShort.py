#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class StringShort(bsvxDataType):
    # Short String  = [1,127] : UTF-8 encoded string of byte length 1-127
    _mask = int('01111111', 2)

    def __init__(self, input):
        self._length = input & self._mask

    # From UTF-8 String to Hex
    def to_binary_encoding(self):
        self._hex_data = hex(int(self._data, 0)) # Int(x, 0) has the 'x' parameter interpreted literally
        return 
    
    # From Hex to UTF-8 String
    def from_binary_encoding(self):
        self._data = bytes.fromhex(self._hex_data).decode('utf-8')
        return