import bsvxpy as bsv
import pytest

test_float = bsv.Float(-1337, 3)

def test_float_init():
    assert test_float._data == -1337
    assert test_float._precision == 3

def test_float_get_data():
    assert test_float.get_data() == -1337

def test_float_get_precision():
    assert test_float.get_precision() == 3

def test_float_set_data():
    test_float.set_data(9001)
    assert test_float._data == 9001

def test_float_set_precision():
    test_float.set_precision(0)
    assert test_float._precision == 0