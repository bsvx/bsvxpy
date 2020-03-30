#!/usr/bin/env python

class bsvxDataType:
    # Private Member variables
    # ------------------------
    _length = None  # (int, base 10) the number of bytes we need to read after reading the size bit 
    _hex_data = None # (int, base 16) the hex representation of the data
    _data = None    # (Subclass dependent) the data representation in the "correct" type, i.e. int for ShortInt, string for ShortString, etc.
    _mask = None    # (int, base 2) corresponding bits in the input byte used to encode length or data
    
    # Constructor
    # -----------
    def __init__(self):
        return

    # Accessor Functions
    # ------------------
    def get_length(self):   # Returns the stored _length variable as a base 10 int
        return self._length
    
    def get_data(self):     # Returns the stored _data variable as a base 16 int
        return self._data

    # I/O Functions
    # -------------
    # fileHandle: the file handle associated with an OPEN file
    # length: the number of half-bytes to read
    def read(self, fileHandle, length = None): # Returns a base 16 int that corresponds to the data read from the file
        input = int("0", 2)
        if length == None:  # Read from a .csv file
            # Read until we encounter a ',' character
            # Convert input to a base 16 int
            pass
        else:               # Read from a .bsv file
            input = fileHandle.read(length) # Already in base 16 format

        return input
    
    def write(self, fileHandle):
            fileHandle.write(self._data)
            return