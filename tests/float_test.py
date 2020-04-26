import bsvxpy as bsv
import pytest

float_header = hex(153).lstrip('0x') # header for floating point data entry (152) that is single precision (1): 152 + 1 = 153
float_test_single = bsv.Float(float_header)

def test_float_single():
    assert float_test_single._precision == 1

double_header = hex(154).lstrip('0x') # header for floating point data entry (152) that is double precision (2): 152 + 2 = 154
float_test_double = bsv.Float(double_header)

def test_float_double():
    assert float_test_double._precision == 2

float_dec = 3.625
init_float_dec = bsv.Float(float_dec)

def test_float_dec():
    assert init_float_dec.get_data() == 3.625
    assert init_float_dec.get_hex_data() == float(3.625).hex().lstrip('0x')

# bsvxFloat does not support alternate hex encoding, and will throw an AttributeError exception when the
#   user attempts to initialize an object with one
float_alt_hex = '0440680000'

def test_float_alt_hex():
    with pytest.raises(AttributeError):
        bsv.Float(float_alt_hex)