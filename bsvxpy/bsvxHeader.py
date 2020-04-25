#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class Header(bsvxDataType):
    # Header = 168 + [0,15] : Beginning of Header with 0-15 fields
    _mask = int('1111', 2)
    _field_count = None     # Number of fields associated with this Header
    
    def __init__(self, input):
        bsvxDataType.__init__(self, input)
        self._field_count = int(input, 16) & self._mask

    # Accessor Functions
    # ------------------
    def get_count(self):
        return self._field_count