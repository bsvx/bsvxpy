#!/usr/bin/env python

from bsvxBlank import Blank
from bsvxBlob import Blob
from bsvxFloat import Float
from bsvxHeader import Header
from bsvxHeaderLong import HeaderLong
from bsvxIntegerShort import IntegerShort
from bsvxRecord import Record
from bsvxRecordLong import RecordLong
from bsvxStringLong import StringLong
from bsvxStringShort import StringShort



class Reader:
    """
    Takes in a .bsvx file and returns a reader object that can iterate over
    rows in a given bsvxfile
    """

    def __init__(self, bsvxfile):
        pass

class Writer:
    """
    Returns a writer object that can convert user python data into BSVX data fields 
    for file writing.
    """
    def __init__(self, bsvx_filename):
        pass

    def writerow(self, data):
        pass