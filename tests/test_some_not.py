from contests import some_not
import pytest


def test_some_not_subscribe():
    assert True & some_not[True, False]

def test_abs_some_not():
    assert abs(some_not[-3, 0, 3])

def test_some_not_logic_and():
    assert some_not[True, False] & True

def test_some_not_arithmetic():
    assert some_not[1, 2, -1] + 1
    assert some_not[1, 2, 3] - 1

def test_some_not_round():
    assert round(some_not[-0.49, -0.1, 0.1, 0.3, 0.49])