from contests import noone
import pytest
import math

def test_noone_logic():
    assert bool(noone[0, False, ''])
    assert noone[False, False] | False

def test_noone_math():
    assert math.ceil(noone[-0.1, -0.99, -0.5])
    assert math.floor(noone[0.99, 0.5, 0.1, 0])

def test_noone_arithmetic():
    assert noone[1, 2, 3] * 0
    assert noone[0, 1, 1.999] // 2

def test_noone_trunc():
    assert math.trunc(noone[-0.5, -0.1, 0.0, 0.5, 0.99])

def test_noone_bitwise():
    assert ~noone[-1,]

def test_noone_arithmetic_more():
    assert noone[2, 3] >> 2
    assert noone[0,] << 13
    assert -noone[0,]
