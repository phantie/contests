'Content tests'

from collections.abc import Iterable

__all__ = ('some', 'every')
__version__ = '0.1'


class InteriorMut:
    def __init__(self, *values):
        assert len(values) > 0
        if len(values) == 1 and isinstance(values[0], Iterable):
            self.value = values[0]
        else:
            self.value = values

    def __str__(self):
        return f'{self.__class__.__name__}<{self.value}>'

class MagicMeths(type):
    def __new__(cls, name, bases, attrs):
        for magicmeth in ('eq', 'ne', 'lt', 'gt', 'ge', 'le'):
            methname = f'__{magicmeth}__'

            def bake_in(methname):
                return lambda self, other: self.get_wrap(methname)(other)

            attrs[methname] = bake_in(methname)

        attrs['__getattr__'] = attrs['get_wrap']

        return super().__new__(cls, name, bases, attrs)


class some(InteriorMut, metaclass = MagicMeths):
    def get_wrap(self, name):
        def wrap(*args, **kwargs):
            return any(getattr(_, name)(*args, **kwargs) for _ in self.value)
        return wrap

class every(InteriorMut, metaclass = MagicMeths):
    def get_wrap(self, name):
        def wrap(*args, **kwargs):
            return all(getattr(_, name)(*args, **kwargs) for _ in self.value)
        return wrap
