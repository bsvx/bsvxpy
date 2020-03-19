#!/usr/bin/env python

class Record:
    def __init__(self, count, data):
        # _count is integer
        self._count = count
        # _data is dictionary
        self._data = data

    def get_count(self):
        return self._count

    def get_data(self):
        return self._data

    def set_count(self, count):
        self._count = count

    def set_data(self, data):
        self._data = data
