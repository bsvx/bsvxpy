#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class Header(bsvxDataType):
    _count = 0
    
    def __init__(self, input):
        mask = int('1111', 2)
        self._count = input & mask

    def get_count(self):
        return self._count