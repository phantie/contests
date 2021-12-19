from contests import *

import math



assert any(i.isupper() for i in 'ABC') == \
    some('Abc').isupper() == \
    True

assert all(i.islower() for i in 'one') == \
    every('one').islower() == \
    True

assert every('111') == '1'
assert some([1, 1, 1, 2, 1]) == 2
assert every([1, 2, 3, 4, 5]) <= 5
assert every([1, 2, 3, 4, 5]) > 0
assert some('bbbbabbb') != 'b'

assert some['(', ')'] == '('
assert some[1,] == 1
assert some([1]) == 1

assert some(([], -1, 0))(bool)
assert some[[], -1, 0](bool)


assert abs(every[-3, 3])
assert abs(some_not[-3, 0, 3])

assert every[1, 2, 3] + 1
assert some_not[1, 2, -1] + 1


assert every[True, True] & True
assert every[True, True] == True
assert some_not[True, False] & True

assert every[True, 1, 2.71828459045]
assert bool(noone[0, False, ''])

assert math.ceil(every[0.5, -1.5])
assert math.ceil(noone[-0.1, -0.99, -0.5])

assert math.floor(every[-0.1, -0.5, 2])
assert math.floor(noone[0.99, 0.5, 0.1, 0])


assert every[5, 7.0, 9] // 2
assert noone[0, 1, 1.999] // 2

assert hash(every[0.0001, 1000])
assert hash(noone[0,])

# commented because of the warning
# assert int(every[1.1, 2.2, 3.3])
# assert int(noone[-0.5, -0.1, 0.0, 0.5, 0.99])

assert math.trunc(every[1.1, 2.2, 3.3])
assert math.trunc(noone[-0.5, -0.1, 0.0, 0.5, 0.99])


assert ~every[0, 1, 2]
assert ~noone[-1,]

assert noone[2, 3] >> 2

assert noone[0,] << 13

assert every[3, 5, 7, 9] % 2
assert noone[2, 4, 6, 8] % 2

assert noone[1, 2, 3] * 0
assert every[1, 2, 3] * 0.1


assert -noone[0,]
assert -every[-1, 1]

assert every[False, False] | True
assert some[False, True] | False
assert noone[False, False] | False

assert +every[1, 2, 3]
assert +noone[0, 0.0]

assert every[0, 1, 2] ** 0
assert noone[0,] ** 13

assert 1 + every[0, 1, 2]
assert 1 + noone[-1,]

assert True | every[False, False]
assert False | some[False, True]
assert False | noone[False, False]


assert True & every[True, True]
assert True & some_not[True, False]


assert round(noone[-0.49, -0.1, 0.1, 0.3, 0.49])

assert noone[0,] / 42

assert some_not[1, 2, 3] - 1

assert every[False, False] ^ True
assert every[True, True] ^ False

def more_than_three(gen):
    for counter, _ in enumerate(filter(bool, gen), start = 1):
        if counter > 2:
            return True 
    return False


three_more = create('three_more', more_than_three)

assert three_more[1, 2, 3] > 0
assert three_more[1, 2, 0] > -1

assert three_more[1, 2, 0]()
assert not three_more[1, 2]()
