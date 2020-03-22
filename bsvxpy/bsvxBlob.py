#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class Blob(bsvxDataType):
    def __init__(self, data, length):
        # _data is bytestring
        self._data = data
        # _length is integer
        self._length = length

    def get_data(self):
        return self._data

    def get_length(self):
        return self._length

    def set_data(self, data):
        self._data = data

    def set_length(self, length):
        self._length = length
