What?
=============

.. code:: python

    assert any(i.isupper() for i in 'ABC') == \
        some('ABC').isupper() == \
        True

    assert all(i.islower() for i in 'one') == \
        every('one').islower() == \
        True

    assert every('111') == '1'
    assert some([1, 1, 1, 2, 1]) == 2
    assert every([1, 2, 3, 4, 5]) <= 5
    assert every([1, 2, 3, 4, 5]) > 0
    assert some('bbbbabbb') != 'b'


Import:

    from contests import some, every