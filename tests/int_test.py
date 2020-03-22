import bsvxpy as bsv
import pytest

test_integer = int('01111011', 2)
int_test = bsv.IntegerShort(test_integer) # not sure if this is how we want to take input, i'll let you decide
if int_test.get_data() == 3:
    print("Integer Test 1 Passed")
else:
    print("Integer Test 1 Failed. Length = ", int_test.get_length())


test_integer = int('7B', 16)
int_test_hex = bsv.IntegerLong(test_integer)
if int_test.get_data() == 3:
    print("Integer Test 2 Passed")
else:
    print("Integer Test 2 Failed. Length = ", int_test.get_length())
