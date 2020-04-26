import bsvxpy as bsv
import pytest

test_string_header = hex(44).lstrip('0x') # 44 in decimal
test_string = "The quick brown fox jumped over the lazy dog"
str_test = bsv.StringShort(test_string_header)

def test_str_short_init():
    assert str_test.get_length() == 44

test_long_std = "81" # 129 in decimal (128 base + 1)
init_long_std = bsv.StringLong(test_long_std)

def test_str_long_std():
    assert init_long_std._long_length == 2

test_long_dec = 129
init_long_dec = bsv.StringLong(test_long_dec)

def test_str_long_dec():
    assert init_long_dec.get_data() == 129
    assert init_long_dec.get_length() == 1