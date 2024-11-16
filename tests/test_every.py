from contests import every
import pytest

def test_every_lower():
    assert every('one').islower() == True

def test_every_single_digit():
    assert every('111') == '1'

def test_every_inequality_lower():
    assert every([1, 2, 3, 4, 5]) <= 5

def test_every_inequality_upper():
    assert every([1, 2, 3, 4, 5]) > 0

def test_abs_every():
    assert abs(every[-3, 3])

def test_every_logic():
    assert every[True, True] & True
    assert every[True, True] == True
    assert every[True, 1, 2.71828459045]()

def test_every_arithmetic():
    assert every[5, 7.0, 9] // 2
    assert every[0, 1, 2] ** 0
    assert 1 + every[0, 1, 2]

def test_every_truncate():
    import math
    assert math.trunc(every[1.1, 2.2, 3.3])

def test_bitwise_operations_every():
    assert ~every[0, 1, 2]    