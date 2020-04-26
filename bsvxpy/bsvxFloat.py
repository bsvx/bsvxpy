#!/usr/bin/env python

from .bsvxDataType import bsvxDataType
from enum import Enum
from struct import pack, unpack

class Float(bsvxDataType):
    # Float = 152 + [0,7] : IEEE-754 format float. 1 = Single, 2 = Double
    _mask = int('111', 2)
    _precision = None       # Stores the float's precision. Preserves role of _length

    def __init__(self, input):
        bsvxDataType.__init__(self, input)
        self._precision = None              # Default value to handle when we don't know the precision of the float

        if type(input) is float:                            # PYTHON FLOAT OBJ INPUT
            self._length = 8
            self._precision = 2
            self._data = input
            self._hex_data = input.hex()
        else:                                               # HEX VALUE FROM BSVX FILE
            self._precision = int(input, 16) & self._mask

            # Determines the Precision of the float       (E/M, bias)              Exponent bits / Significand bits
            # -----------------------------------------------------------------------------------------------------
            if self._precision == 1:     # (8/24, exp. bias: 127)       0000 0000 / 0000 0000 0000 0000 0000 0000
                self._length = 4
            elif self._precision == 2:   # (11/53, exp. bias: 1023) 0000 0000 000 / 0 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
                self._length = 8


    def set_data(self, data=None):
        if data == None:
            self.from_IEEE(self._hex_data)
        else:
            self.from_IEEE(data)
        return



    # Helper Functions
    # ----------------
    # Conversion functions are meant to be called after a Read() function has read in the data

    # Converts IEEE-754 floats to Binary representation
    def from_IEEE(self, data):
        if (self._precision == 1):
            self._data = unpack('>f', bytes.fromhex(data))[0]
        elif (self._precision == 2):
            self._data = unpack('>d', bytes.fromhex(data))[0]

    # Converts Binary floats to IEEE-754 representation
    def to_IEEE(self, data):
        if (self._precision == 1):
            self._data = pack('f', data)
        elif (self._precision == 2):
            self._data = pack('d', data)