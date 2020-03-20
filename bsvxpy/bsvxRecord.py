#!/usr/bin/env python

from bsvxpy import bsvxDataType

class Record(bsvxDataType):
    _count = 0
    
    def __init__(self, input):
        mask = bytearray("0F")
        self._count = int.from_bytes(input & mask)

    def get_count(self):
        return self._count