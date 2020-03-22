import bsvxpy as bsv
import pytest

test_float = bsv.Float(-1337)

def test_float_init():
    print(test_float._data)
