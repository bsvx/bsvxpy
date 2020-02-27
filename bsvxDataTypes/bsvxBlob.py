#!/usr/bin/env python

class Blob:
    def __init__(self, data, length):
        # _data is bytestring
        self._data = self.set_data(data)
        # _length is integer
        self._length = self.set_length(length)

    def get_data(self):
        return self._data

    def get_length(self):
        return self._length

    def set_data(self, data):
        self._data = data

    def set_length(self, length):
        self._length = length
