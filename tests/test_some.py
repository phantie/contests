from contests import some
import pytest

def test_some_upper():
    assert some('Abc').isupper() == True

def test_some_element():
    assert some([1, 1, 1, 2, 1]) == 2

def test_some_not_b():
    assert some('bbbbabbb') != 'b'

def test_some_tuple():
    assert some(([], -1, 0))(bool)

def test_some_mixed():
    assert some([[], -1, 0])(bool)
    
def test_some_list():
    assert some([1]) == 1

def test_some_single_element_list():
    assert some[1,] == 1

def test_some_parentheses():
    assert some['(', ')'] == '('