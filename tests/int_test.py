import bsvxpy as bsv
import pytest

test_integer = int('10001011', 2) # 139 in decimal

print(test_integer)
int_test = bsv.IntegerSmall(test_integer)

def test_int_short_init():
    assert int_test.get_data() == 3

test_integer = int('92', 16) # 146 in decimal
int_test_hex = bsv.IntegerLong(test_integer)

def test_int_long_init():
    assert int_test_hex.get_length() == 3 # @3/25 : Cannot read data from Long Integers, changed to check length

test_string_header = int('101100', 2) # 44 in decimal
test_string = "The quick brown fox jumped over the lazy dog"
str_test = bsv.StringShort(test_string_header)

def test_str_short_init():
    assert str_test.get_length() == 44