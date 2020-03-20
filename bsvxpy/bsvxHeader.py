#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class Header(bsvxDataType):
    _count = 0
    
    def __init__(self, input):
        mask = bytearray("0F")
        self._count = int.from_bytes(input & mask)

    def get_count(self):
        return self._count