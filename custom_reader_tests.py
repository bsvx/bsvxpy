import bsvxpy
import csv

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

obj_list = []
with open("custom_sample.bsvx", 'r') as fHandle:
        header = fHandle.read(2)
        while header != '':
            headerBinary = int(header, 16)
            data_type = _parse_type(None, headerBinary)
            obj_list.append(_init_bsv_object(None, data_type, header))
            if obj_list[-1].is_long():
                obj_list[-1].read_length(fHandle)
            if obj_list[-1].get_length() != 0:
                obj_data = fHandle.read(obj_list[-1].get_length() * 2)
                obj_list[-1].set_data(obj_data)
            print("Header: ", header)
            print("Data Type: ", data_type)
            print("Stored Data: ", obj_list[-1].get_data())
            header = fHandle.read(2)
        fHandle.close()

with open("custom_output.csv", 'w', newline='') as fHandle:
    obj_data = [obj.get_data() for obj in obj_list]
    writer = csv.writer(fHandle)
    writer.writerow(obj_data)
    fHandle.close()