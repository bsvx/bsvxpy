#!/usr/bin/env python

from bsvxRecord import Record

class RecordLong(Record):
    def __init__(self, count, data, length):
        # _count is integer
        # _data is dictionary
        super().__init__(count, data)
        # _length is integer
        self._length = self.set_length(length)

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length
