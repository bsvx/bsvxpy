#!/usr/bin/env python

from bsvxDataTypes.bsvxHeader import Header

class HeaderLong(Header):
    def __init__(self, count, data, length):
        # _count is integer
        # _data is dictionary
        super().__init__(count, data)
        # _length is integer
        self._length = length

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length
