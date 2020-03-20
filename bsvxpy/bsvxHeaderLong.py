#!/usr/bin/env python

from .bsvxHeader import Header

class HeaderLong(Header):
    _count = 0
    _long_length = 0
    def __init__(self, input):
        mask = bytearray("07")
        self._long_length = int.from_bytes(input & mask) + 1

        self._count = int.from_bytes(self.read(None, self._long_length))

    def get_count(self):
        return self._count