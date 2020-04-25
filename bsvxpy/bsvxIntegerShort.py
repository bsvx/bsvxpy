#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class IntegerShort(bsvxDataType):
    # Small Int = 136 + [0, 7] : An integer in the range 0-7
    _mask = int('111', 2)

    # IntegerShort's _data and _hex_data values will be identical due to binary encoding of decimal integers
    # This results in no decoding b/w _hex_data and _data assignments.
    # __init__ structure preserved for congruency throughout library
    def __init__(self, input):
        bsvxDataType.__init__(self, input)
        self._length = 0
        
        try:                                            # HEX BYTE FOR READING FROM FILE
            self._data = int(input, 16) & self._mask
            self._hex_data = str(self._data)
        except TypeError:                               # REGULAR INTEGER INPUT
            self._data = input          # Because IntegerShort only corresponds to decimal values 0-7
            self._hex_data = input      # both _data and _hex_data will be the same
        
        return