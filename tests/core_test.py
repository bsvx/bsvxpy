import bsvxpy as bsv
from bsvxpy import core
import pytest

test_reader = bsv.Reader("test_file.bsvx")
test_writer = bsv.Writer()

def test_core_reader():
    assert test_reader._bsvxfile_path == "test_file.bsvx"

def test_core_reader_wrong_init():
    with pytest.raises(Exception):
        core.Reader("test_file.txt") # this should raise an exception

def test_core_reader_readrow():
    assert test_reader.readrow()._count == -1
    assert test_reader.readrow()._data == 0

def test_core_writer_writerow_wrong_path():
    with pytest.raises(Exception):
        core.Writer(data=1,bsvxfile="test_file.txt") # this should raise an exception

def test_core_writer_writerow():
    assert test_writer.writerow(data=1, bsvxfile="test_file.bsvx") == True