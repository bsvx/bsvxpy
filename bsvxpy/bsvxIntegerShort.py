#!/usr/bin/env python

import bsvxpy

class IntegerShort(bsvxpy.bsvxDataType):
    def __init__(self, input):
        mask = bytearray("07")
        self._length = 0
        self._data = int.from_bytes(input & mask)