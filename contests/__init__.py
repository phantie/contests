'Content tests'

__all__ = ('some', 'every', 'noone', 'some_not', 'create')
__version__ = '0.2'

import math



class InteriorMut:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.__class__.__name__}<{self.value}>'

    def __class_getitem__(cls, item):
        return cls(item)


supported_magic_methods = [
    'eq', 'ne', 'lt', 'gt', 'ge', 'le',
    'abs', 'add', 'and', 'bool', 'ceil',
    'floor', 'floordiv', 'hash', 'int',
    'invert', 'rshift', 'lshift', 'mod',
    'mul', 'neg', 'or', 'pos', 'pow', 'radd',
    'ror', 'rand', 'rlshift', 'rmod', 'rmul',
    'round', 'rpow', 'rrshift', 'rsub', 'truediv',
    'rtruediv', 'rxor', 'sub', 'trunc', 'xor',
]


class MagicMeths(type):
    def __new__(cls, name, bases, attrs):
        magicmeth_to_func = dict(
            bool = bool,
            abs = abs,
            ceil = math.ceil,
            floor = math.floor,
            hash = hash,
            int = int,
            trunc = math.trunc,
        )

        for magicmeth in supported_magic_methods:
            if magicmeth in magicmeth_to_func:
                def bake_in(magicmeth):
                    return lambda self: self.__call__(magicmeth_to_func[magicmeth])
            else:
                def bake_in(magicmeth):
                    return lambda self, *args, **kwargs: self.get_wrap(f'__{magicmeth}__')(*args, **kwargs)

            attrs[f'__{magicmeth}__'] = bake_in(magicmeth)

        attrs['__getattr__'] = attrs['get_wrap']

        return super().__new__(cls, name, bases, attrs)

def create(name, f):
    class cls(InteriorMut, metaclass = MagicMeths):
        def get_wrap(self, name):
            def wrap(*args, **kwargs):
                return f(getattr(_, name)(*args, **kwargs) for _ in self.value)
            return wrap
        
        __call__ = lambda self, lam = lambda item: True, /: f(lam(_) for _ in self.value)

    cls.__name__ = name
    cls.__qualname__ = name
    return cls

def complement(f):
    """Takes a fn f and returns a fn that takes the same arguments as f,
    has the same effects, if any, and returns the opposite truth value."""
    def wrap(*args, **kwargs):
        return not f(*args, **kwargs)
    return wrap

some = create('some', any)
every = create('every', all)
some_not = create('some_not', complement(all))
noone = create('noone', complement(any))


