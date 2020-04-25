import bsvxpy as bsv
import pytest

test_integer = hex(139) # 139 in decimal
int_test = bsv.IntegerShort(test_integer)

def test_int_short_init():
    assert int_test.get_data() == 3

test_integer_dec = 7
int_test_dec = bsv.IntegerShort(test_integer_dec)
def test_int_short_dec_input():
    assert int_test_dec.get_data() == 7

test_integer = hex(146) # 146 in decimal
int_test_hex = bsv.IntegerLong(test_integer)

def test_int_long_init():
    assert int_test_hex.get_length() == 3 # @3/25 : Cannot read data from Long Integers, changed to check length