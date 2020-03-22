#!/usr/bin/env python

from .bsvxRecord import Record

class RecordLong(Record):
    _count = 0
    _long_length = 0
    def __init__(self, input):
        mask = int('111', 2)
        self._long_length = input & mask

        self._count = int(self.read(None, self._long_length), 16)

    def get_count(self):
        return self._count