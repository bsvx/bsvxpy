#!/usr/bin/env python

from bsvxDataTypes.bsvxStringShort import StringShort

class StringLong(StringShort):
    def __init__(self, data, length):
        # _data is string
        super().__init__(data)
        # _length is integer
        self._length = length

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length= length
