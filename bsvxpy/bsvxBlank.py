#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class Blank(bsvxDataType):
    # Blank = 0 + [0,0]
    
    def __init__(self):
        bsvxDataType.__init__(self, '0')
        self._length = 0
        return
