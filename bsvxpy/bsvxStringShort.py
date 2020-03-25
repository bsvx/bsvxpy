#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class StringShort(bsvxDataType):
    # Short String  = [1,127] : UTF-8 encoded string of byte length 1-127
    _mask = int('01111111', 2)

    def __init__(self, input):
        self._length = input & self._mask