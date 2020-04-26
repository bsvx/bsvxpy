#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class StringShort(bsvxDataType):
    # Short String  = [1,127] : UTF-8 encoded string of byte length 1-127
    _mask = int('01111111', 2)

    def __init__(self, input):
        bsvxDataType.__init__(self, input)
        try:                                                    # HEX BYTE FOR READING FROM FILE
            self._length = int(input, 16) & self._mask
        except ValueError:                                      # REGULAR STRING INPUT
            self._length = len(input)
            self._data = input
            self._hex_data = bytes.hex(input.encode('utf-8'))

    def set_data(self, data=None):
        self.from_binary_encoding(data)

    # From UTF-8 String to Hex
    def to_binary_encoding(self):
        self._hex_data = hex(int(self._data, 0)) # Int(x, 0) has the 'x' parameter interpreted literally
        return 
    
    # From Hex to UTF-8 String
    def from_binary_encoding(self, data = None):
        if data != None:
            self._data = str(bytes.fromhex(data).decode('utf-8'))
        else:
            self._data = str(bytes.fromhex(self._hex_data).decode('utf-8'))
        return