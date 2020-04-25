import bsvxpy as bsv
import pytest

test_string_header = hex(44) # 44 in decimal
test_string = "The quick brown fox jumped over the lazy dog"
str_test = bsv.StringShort(test_string_header)

def test_str_short_init():
    assert str_test.get_length() == 44

test_string_hex_with_length = "03464F4F"
string_test_hex_with_length = bsv.StringShort(test_string_hex_with_length)

def test_str_short_hex_with_length_init():
    assert string_test_hex_with_length.get_length() == 3
    assert string_test_hex_with_length.get_data() == "FOO"