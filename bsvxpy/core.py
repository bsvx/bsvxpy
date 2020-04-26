#!/usr/bin/env python

import bsvxpy
import csv

class Reader:
    """
    Takes in a .bsvx file and returns a reader object that can iterate over
    rows in a given bsvxfile
    """
    def __init__(self, file_name, format='r'):
        self._file_name = file_name
        self._format = format
        self._obj_list = []

    def read(self, file_type='bsvx'):
        if file_type == 'bsvx':
            with open(self._file_name, self._format) as fHandle:
                header = fHandle.read(2)
                while header != '':
                    self._obj_list.append(self._init_bsv_object(header))
                    if self._obj_list[-1].is_long():
                        self._obj_list[-1].read_length(fHandle)
                    if self._obj_list[-1].get_length() != 0:
                        obj_data = fHandle.read(self._obj_list[-1].get_length() * 2)
                        self._obj_list[-1].set_data(obj_data)
                    header = fHandle.read(2)
        if file_type == 'csv':
            raise AttributeError('The .csv file format is not currently supported for reading')
        
        return self._obj_list.copy()

    def _init_bsv_object(self, obj_header):
        obj_length = int(obj_header, 16)
        if 0 <= obj_length < 1:
            return bsvxpy.Blank()
        elif 1 <= obj_length < 128:
            return bsvxpy.StringShort(obj_header)
        elif 128 <= obj_length < 135:
            return bsvxpy.StringLong(obj_header)
        elif 135 <= obj_length < 144:
            return bsvxpy.IntegerShort(obj_header)
        elif 144 <= obj_length < 152:
            return bsvxpy.IntegerLong(obj_header)
        elif 152 <= obj_length < 160:
            return bsvxpy.Float(obj_header)
        elif 160 <= obj_length < 168:
            return bsvxpy.Blob(obj_header)
        elif 168 <= obj_length < 184:
            return bsvxpy.Header(obj_header)
        elif 184 <= obj_length < 192:
            return bsvxpy.HeaderLong(obj_header)
        elif 192 <= obj_length < 208:
            return bsvxpy.Record(obj_header)
        elif 208 <= obj_length < 216:
            return bsvxpy.RecordLong(obj_header)
        else:
            raise ValueError("Object header not recognized: ", obj_header)


class Writer:
    """
    Returns a writer object that can convert user python data into BSVX data fields 
    for file writing.
    """
    def __init__(self, file_name, obj_list, format='w'):
        self._file_name = file_name
        self._format = format
        self._obj_list = obj_list.copy()

    def write(self, file_type='csv'):
        with open(self._file_name, self._format) as fHandle:
            if file_type == 'csv':
                obj_data = [obj.get_data() for obj in self._obj_list]
                writer = csv.writer(fHandle)
                writer.writerow(obj_data)
            elif file_type == 'bsvx':
                raise AttributeError('The .bsvx file format is not currently supported for writing')

        return


