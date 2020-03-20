#!/usr/bin/env python

from .bsvxHeader import Header

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

    def readrow(self):
        """
        Reads a line from the given file and returns its value. 
        Expected behavior: returns a header containing the 
        """
        # header to return, has garbage values for testing purposes for now
        # TODO: implement this to actually loop through data
        ret = Header(-1, 0)
        return ret

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
