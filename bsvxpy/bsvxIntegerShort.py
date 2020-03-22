#!/usr/bin/env python
from .bsvxDataType import bsvxDataType
class IntegerShort(bsvxDataType):
    def __init__(self, data):
        mask = bytearray("07", encoding='utf-8') # maybe we can use ints instead of bytearrays
        self._length = 0
        self._data = int.from_bytes(bytearray(data) & mask) # cause this does not worrk
        