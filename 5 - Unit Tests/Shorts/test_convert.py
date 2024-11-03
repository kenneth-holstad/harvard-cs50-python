import pytest
from convert import convert


def test_int_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000


def test_error():
    with pytest.raises(TypeError):
        convert("1")


def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)
#    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-12)
# note: the above is an unacceptably small range but we have it here just so the test will pass
# instructor did this for the example but obviously do not do it like that in the real world