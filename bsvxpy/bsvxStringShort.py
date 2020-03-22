#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class StringShort(bsvxDataType):

    def __init__(self, input):
        mask = int('111', 2)
        self._length = int.from_bytes(input & mask)
        
        # _data is string
        self._data = (self.read(None, self._length)).decode('utf-8')