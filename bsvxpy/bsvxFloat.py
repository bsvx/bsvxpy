#!/usr/bin/env python

from bsvxpy import bsvxDataType

class Float(bsvxDataType):
    def __init__(self, input):
        mask = bytearray("07")
        self._length = int.from_bytes(input & mask)

        if self._length == 1:
            self._data = float.fromhex(self.read(None, 32).hex())
        elif self._length == 2:
            self._data = float.fromhex(self.read(None, 64).hex())