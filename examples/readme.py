from contests import some, every, some_not, noone

assert some("Abc").isupper() == any(i.isupper() for i in "Abc")
assert every("one").islower() == all(i.islower() for i in "one")
assert some_not("Abc").islower() == (not all(i.islower() for i in "Abc"))
assert noone("abc").isupper() == (not any(i.isupper() for i in "abc"))

assert some([1, 1, 1, 2, 1]) == 2
assert every([1, 2, 3, 4, 5]) > 0
assert some("bbbbabbb") != "b"

assert some["(", ")"] == "("
assert some([1]) == 1