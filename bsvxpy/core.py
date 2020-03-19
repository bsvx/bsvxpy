#!/usr/bin/env python

from . import bsvxBlank
from . import bsvxBlob
from . import bsvxFloat
from . import bsvxHeader
from . import bsvxHeaderLong
from . import bsvxIntegerLong
from . import bsvxIntegerShort
from . import bsvxRecord
from . import bsvxRecordLong
from . import bsvxStringLong
from . import bsvxStringShort


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

def blank():
    return bsvxBlank.Blank()