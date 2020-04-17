#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class Reader:
    """
    Takes in a .bsvx file and returns a reader object that can iterate over
    rows in a given bsvxfile
    """

    def __init__(self, bsvxfile):
        """
        Initialization for Reader class, takes in a file as a parameter and can be traversed using readrow
        """
        if not bsvxfile.endswith(".bsvx"):
            raise Exception("File supplied to Reader is not a .bsvx file. File directory given:{}".format(bsvxfile))
        self._bsvxfile_path = bsvxfile

    def read(self):
        file_obj = open(self._bsvxfile_path, "r")
        text_buf = file_obj.readrow() #change to read in 2 characters as integers
        self._parse_type(text_buf)
    
    def _parse_type(self, text_buffer):
        field_length = self._hex_to_dec(text_buffer[:2])
        for i in range(0, field_length): # field_length is how many records are in each row
            #iterate over the row
            pass # implement switching on type


    def _hex_to_dec(self, hex_string):
        i = int(hex_string, 16)
        return str(i)

class Writer:
    """
    Returns a writer object that can convert user python data into BSVX data fields 
    for file writing.
    """
    def __init__(self):
        pass

    def writerow(self, data, bsvxfile):
        """
        Returns True when it is able to write a row to a file.
        Usage: Provide bsvx data and file path to function and it will write the bit representation
        to the given file.
        """
        if not bsvxfile.endswith(".bsvx"):
            raise Exception("File supplied to writerow is not a .bsvx file. File directory given:{}".format(bsvxfile))
        return True
