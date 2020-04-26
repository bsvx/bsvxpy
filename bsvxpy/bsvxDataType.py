#!/usr/bin/env python

class bsvxDataType:
    # Private Member variables
    # ------------------------
    _input = None #(int, base 10) the type 0-255. See _data_types_list for reference
    _length = None  # (int, base 10) the number of bytes we need to read after reading the size bit 
    _hex_data = None # (int, base 16) the hex representation of the data
    _data = None    # (Subclass dependent) the data representation in the "correct" type, i.e. int for ShortInt, string for ShortString, etc.
    _mask = None    # (int, base 2) corresponding bits in the input byte used to encode length or data
    _data_types_list = {
        0:'blank',
        1:'string',
        128:'string_long',
        135:'int_short',
        144:'int_long',
        152:'float',
        160:'blob',
        168:'header',
        184:'header_long',
        192:'record',
        208:'record_long',
        216:'reserved'} # permanent spot for parsing data types, static list of all types and their values.
    _long_type = False
    
    # Constructor
    # -----------
    def __init__(self, hex_data):
        self._hex_data = hex_data

    # Accessor Functions
    # ------------------
    def get_length(self):   # Returns the stored _length variable as a base 10 int
        return self._length
    
    def get_data(self):     # Returns the stored _data variable as a base 16 int
        return self._data

    def get_hex_data(self):
        return self._hex_data
    
    def get_type(self):
        return self._input

    def is_long(self):
        return self._long_type

    # Mutator Functions
    # ------------------
    def set_hex_data(self, data):
        self._hex_data = data
        return
    
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

    # Helper Functions
    # ----------------
    # returns the binary value associated with the subclasses datatype
    # INPUT: operates on the _data member variable
    # EFFECTS: assigns new value to _hex_data member variable
    def to_binary_encoding(self):
        self._hex_data = int(self._data, 0)
        return 

    # returns the typed value associated with the subclasses datatype
    # INPUT: operates on the _hex_data member variable
    # EFFECTS: assigns new value to _data member variable
    def from_binary_encoding(self):
        self._data = self._hex_data
        return
