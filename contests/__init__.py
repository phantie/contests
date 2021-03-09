'Content tests'

class InteriorMut:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.__class__.__name__}<{self.value}>'


class MagicMeths: ...
    # __eq__ = lambda self, other: 
    # __ne__ = lambda self, other: 

class some(InteriorMut, MagicMeths):
    def __getattr__(self, name):
        return self.get_wrap(name)

    def get_wrap(self, name):
        def wrap(*args, **kwargs):
            return any(getattr(_, name)(*args, **kwargs) for _ in self.value)
        return wrap

class every(InteriorMut, MagicMeths):
    def __getattr__(self, name):
        return self.get_wrap(name)

    def get_wrap(self, name):
        def wrap(*args, **kwargs):
            return all(getattr(_, name)(*args, **kwargs) for _ in self.value)
        return wrap

assert any(i.isupper() for i in 'ABC') == \
       some('ABC').isupper() == \
       True

assert all(i.islower() for i in 'one') == \
       every('one').islower() == \
       True

# assert every('111') == '1'