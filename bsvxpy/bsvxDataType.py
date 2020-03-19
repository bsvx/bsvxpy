
class bsvxDataType:
    _length = None
    _data = None

    def __init__(self):
        return

    def get_length(self):
        return self._length
    
    def get_data(self):
        return self._data

    def read(self, fileHandle, length):
        return bytearray('00')