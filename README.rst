What?
=============

.. code:: python

    from contests import some, every

    assert any(i.isupper() for i in 'ABC') == \
        some('ABC').isupper() == \
        True

    assert all(i.islower() for i in 'one') == \
        every('one').islower() == \
        True