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
        self._length = 0                    # Short Int does not read data from file
        #self._hex_data = int(input, 16) & self._mask # hex_data is the 0 - 7 value encoded in the input byte
        # The above line returns 0 for when I try to instantiate an object, commenting it out for now.
        self.from_binary_encoding()       
        return