import bsvxpy as bsv
import pytest

test_integer = int('01111011', 2)
int_test = bsv.IntegerShort(test_integer) # not sure if this is how we want to take input, i'll let you decide

def test_int_short_init():
    assert int_test.get_data() == 3

test_integer = int('7B', 16)
int_test_hex = bsv.IntegerLong(test_integer)

def test_int_long_init():
    assert int_test_hex.get_data() == 0 # this needs to be changed, simply a stub for now

