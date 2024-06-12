from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("9/2")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
