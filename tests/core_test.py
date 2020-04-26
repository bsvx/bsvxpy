import bsvxpy as bsv
from bsvxpy import core
import pytest

test_reader = bsv.Reader("test_input.bsvx")
obj_list = test_reader.read()
print(obj_list)
test_writer = bsv.Writer('test_output.csv', obj_list)

test_reader.read()
test_writer.write()