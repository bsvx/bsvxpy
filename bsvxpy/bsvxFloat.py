#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class Float(bsvxDataType):
    def __init__(self, input):
        mask = int('111', 2)
        self._length = input & mask

        if self._length == 0:
            self._data = float.fromhex(self.read(None, 2))
        elif self._length == 1:
            self._data = float.fromhex(self.read(None, 4))
        elif self._length == 2:
            self._data = float.fromhex(self.read(None, 8))
        elif self._length == 3:
            self._data = float.fromhex(self.read(None, 16))