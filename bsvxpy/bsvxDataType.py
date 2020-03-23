#!/usr/bin/env python

class bsvxDataType:
    _length = None # the number of bytes we need to read after reading the size bit
    _data = None # the hex representation of the data
    
    
    def __init__(self):
        return

    def get_length(self):
        return self._length
    
    def get_data(self):
        # convert from binary/hex to decimal
        return self._data

    def read(self, fileHandle, length):
        # return to the object the hex representation of the data we read
        # the data will be as long as length is
        return hex(0) 
    
    def write(self, fileHandle):
        with open(fileHandle) as file:
            file.write(self._data)