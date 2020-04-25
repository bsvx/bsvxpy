import bsvxpy as bsv
import pytest

float_header = hex(153) # header for floating point data entry (152) that is single precision (1): 152 + 1 = 153

print(float_header)
float_test_single = bsv.Float(float_header)

def test_float_single():
    assert float_test_single._precision == 1

float_header = hex(154) # header for floating point data entry (152) that is double precision (2): 152 + 2 = 154
float_test_double = bsv.Float(float_header)

def test_float_double():
    assert float_test_double._precision == 2 # @3/25 : Cannot read data from Long Integers, changed to check length