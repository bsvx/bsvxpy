#!/usr/bin/env python

class StringShort:
    def __init__(self, data):
        # _data is string
        self._data = data

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
