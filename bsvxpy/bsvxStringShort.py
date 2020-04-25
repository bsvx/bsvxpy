#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class StringShort(bsvxDataType):
    # Short String  = [1,127] : UTF-8 encoded string of byte length 1-127
    _mask = int('01111111', 2)

    def __init__(self, input):
        bsvxDataType.__init__(self, input)
        try:
            input = input.lstrip('0x')                          # Make sure there is no leading '0x' on the hex input
            if len(input) > 2:                                  # HEX WITH LEADING LENGTH VALUE
                self._length = int(input[0:1], 16)
                self._hex_data = input[1:len(input)]
                self.from_binary_encoding()
            else:                                               # HEX BYTE FOR READING FROM FILE
                self._length = int(input, 16) & self._mask
        except ValueError:                                      # REGULAR STRING INPUT
            self._length = len(input)
            self._data = input
            self._hex_data = input.hex()

    # From UTF-8 String to Hex
    def to_binary_encoding(self):
        self._hex_data = hex(int(self._data, 0)) # Int(x, 0) has the 'x' parameter interpreted literally
        return 
    
    # From Hex to UTF-8 String
    def from_binary_encoding(self):
        print(self._hex_data)
        self._data = bytes.fromhex(self._hex_data).decode('utf-8')
        return