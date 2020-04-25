#!/usr/bin/env python

import bsvxpy

class Reader:
    """
    Takes in a .bsvx file and returns a reader object that can iterate over
    rows in a given bsvxfile
    """
    _bsvxfile_path = ""
    _text_buf = ""


    def __init__(self, bsvxfile):
        """
        Initialization for Reader class, takes in a file as a parameter and can be traversed using readrow
        """
        if not bsvxfile.endswith(".bsvx"):
            raise Exception("File supplied to Reader is not a .bsvx file. File directory given:{}".format(bsvxfile))
        self._bsvxfile_path = bsvxfile

    def read(self):
        obj_list = []
        file_obj = open(self._bsvxfile_path, "r")
        self._text_buf = file_obj.readline() # Read first row of the file, and any subsequent rows later
        length = self._parse_length(0)
        text_index = 2 # after the first two characters for row length are read in, we begin reading object data from the 2nd index
        for i in range(0, int(length)): # field_length is how many records are in each row
            #iterate over the row
            text_index = self._parse_data(text_index, obj_list)
        return obj_list
    
    def _parse_length(self, text_index):
        return self._hex_to_dec(self._text_buf[text_index:text_index + 2])

    def _parse_data(self, text_index, object_list):
        new_index = text_index # update and return text_index as we go along to keep track of the beginning of a new object
        obj_length = self._parse_length(new_index) # find length of object
        obj_length = int(obj_length)
        new_index = new_index + 2 # iterate index
        obj_type = self._parse_type(obj_length) # find type of object given length
        obj_data = self._text_buf[new_index:new_index + (obj_length * 2)]
        object_list.append(self._init_bsv_object(obj_type, obj_data))
        return new_index + (obj_length * 2)

    def _parse_type(self, obj_length):
        if 0 <= obj_length < 1:
            return bsvxpy.bsvxDataType._data_types_list[0]
        elif 1 <= obj_length < 128:
            return bsvxpy.bsvxDataType._data_types_list[1]
        elif 128 <= obj_length < 135:
            return bsvxpy.bsvxDataType._data_types_list[128]
        elif 135 <= obj_length < 144:
            return bsvxpy.bsvxDataType._data_types_list[135]
        elif 144 <= obj_length < 152:
            return bsvxpy.bsvxDataType._data_types_list[144]
        elif 152 <= obj_length < 160:
            return bsvxpy.bsvxDataType._data_types_list[152]
        elif 160 <= obj_length < 168:
            return bsvxpy.bsvxDataType._data_types_list[160]
        elif 168 <= obj_length < 184:
            return bsvxpy.bsvxDataType._data_types_list[168]
        elif 184 <= obj_length < 192:
            return bsvxpy.bsvxDataType._data_types_list[184]
        elif 192 <= obj_length < 208:
            return bsvxpy.bsvxDataType._data_types_list[192]
        elif 208 <= obj_length < 216:
            return bsvxpy.bsvxDataType._data_types_list[208]
        else:
            return -1

    def _init_bsv_object(self, obj_type, obj_data):
        if obj_type == "blank":
            return bsvxpy.Blank()
        elif obj_type == "string":
            return bsvxpy.StringShort(obj_data)
        elif obj_type == "string_long":
            return bsvxpy.StringLong(obj_data)
        elif obj_type == "int_short":
            return bsvxpy.IntegerShort(obj_data)
        elif obj_type == "int_long":
            return bsvxpy.IntegerLong(obj_data)
        elif obj_type == "float":
            return bsvxpy.Float(obj_data)
        elif obj_type == "blob":
            return bsvxpy.Blob(obj_data)
        elif obj_type == "header":
            return bsvxpy.Header(obj_data)
        elif obj_type == "header_long":
            return bsvxpy.HeaderLong(obj_data)
        elif obj_type == "record":
            return bsvxpy.Record(obj_data)
        elif obj_type == "record_long":
            return bsvxpy.RecordLong(obj_data)
        elif obj_type == "reserved":
            return -1

    def _hex_to_dec(self, hex_string):
        if hex_string == '':
            hex_string = '0'
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
    
        type = self.get_type()
		length = self.get_length()
		
		data.to_binary_encoding(data)
		if(f = open(bsvxfile, 'ab') != 1)
			raise Exception("Failed to open file for appending bytes. File given: " + bsvxfile)
		
		#this needs a switch statement or if-else similar to parse_type. 
		#I'll implement it tonight but I didn't have time.
		#this should work for short string and long int
		f.write(bytes[data.get_hex_data()])
		if(type >= 1 && type <= 127)
			f.write(bytes(data.get_data(), 'utf-8')
		elif(type >= 144 && type <= 151)
			f.write(bytes[data.get_data()])
		
		f.close()
