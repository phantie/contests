from .interior_mut import InteriorMut
from .magic_methods import MagicMeths


def create(name, f):
    class cls(InteriorMut, metaclass=MagicMeths):
        def get_wrap(self, name):
            def wrap(*args, **kwargs):
                return f(getattr(_, name)(*args, **kwargs) for _ in self.value)
            return wrap

        __call__ = lambda self, lam=lambda item: True, /: f(lam(_) for _ in self.value)

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