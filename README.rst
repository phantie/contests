
.. code:: python

    from contests import some, every, some_not, noone

    assert any(i.isupper() for i in 'Abc') == some('Abc').isupper()
    assert all(i.islower() for i in 'one') == every('one').islower()
    assert some_not('Abc').islower()
    assert noone('abc').isupper()

    assert some([1, 1, 1, 2, 1]) == 2
    assert every([1, 2, 3, 4, 5]) > 0
    assert some('bbbbabbb') != 'b'

    assert some['(', ')'] == '('
    assert some([1]) == 1


Install:
::

    pip install git+https://github.com/phantie/contests.git -U


Import:
::

    from contests import some, every, some_not, noone



