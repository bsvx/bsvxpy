#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class Record(bsvxDataType):
    # Reader = 192 + [0,15] : Beginning of Record with 0-15 fields
    _mask = int('1111', 2)
    _field_count = None     # Number of fields associated with this Record
    
    def __init__(self, input):
        self._field_count = int(input, 16) & self._mask

    # Accessor Functions
    # ------------------
    def get_count(self):
        return self._field_count