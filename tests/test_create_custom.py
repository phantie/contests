from contests import create
import pytest


def more_than_three(gen):
    for counter, _ in enumerate(filter(bool, gen), start = 1):
        if counter > 2:
            return True 
    return False


three_more = create('three_more', more_than_three)


def test_three_more():
    assert three_more[1, 2, 3] > 0
    assert three_more[1, 2, 0] > -1
    assert three_more[1, 2, 0]()
    assert not three_more[1, 2]()

