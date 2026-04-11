import pytest
import argparse
from genqr.main import positive_int

def test_positive_int_valid():
    assert positive_int("10") == 10
    assert positive_int("1") == 1

def test_positive_int_invalid_non_positive():
    with pytest.raises(argparse.ArgumentTypeError, match="0 is not a positive integer"):
        positive_int("0")
    with pytest.raises(argparse.ArgumentTypeError, match="-5 is not a positive integer"):
        positive_int("-5")

def test_positive_int_invalid_non_integer():
    with pytest.raises(argparse.ArgumentTypeError, match="abc is not a valid integer"):
        positive_int("abc")
    with pytest.raises(argparse.ArgumentTypeError, match="1.5 is not a valid integer"):
        positive_int("1.5")
