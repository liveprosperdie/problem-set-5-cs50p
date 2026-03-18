from fuel import convert 
from fuel import gauge
import pytest

def test_negative():
    with pytest.raises(ValueError):
        assert convert("-1/5")==ValueError
        assert convert("1/-5")==ValueError


def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")==ZeroDivisionError


def test_float():
    with pytest.raises(ValueError):
        assert convert("1.5/5")== ValueError


def test_correct():
    assert convert ("2/3")==67

def test_x_greater():
    with pytest.raises(ValueError):
        assert convert("5/3")==ValueError


def test_gauge():
    assert gauge(0)=="E"
    assert gauge(99)=="F"
    assert gauge(67)=="67%"


