supported_magic_methods = [
    'eq', 'ne', 'lt', 'gt', 'ge', 'le', 'abs', 'add', 'and', 'bool', 'ceil',
    'floor', 'floordiv', 'hash', 'int', 'invert', 'rshift', 'lshift', 'mod',
    'mul', 'neg', 'or', 'pos', 'pow', 'radd', 'ror', 'rand', 'rlshift', 'rmod',
    'rmul', 'round', 'rpow', 'rrshift', 'rsub', 'truediv', 'rtruediv', 'rxor',
    'sub', 'trunc', 'xor',
]


class MagicMeths(type):
    def __new__(cls, name, bases, attrs):
        import math

        magicmeth_to_func = dict(
            bool=bool,
            abs=abs,
            ceil=math.ceil,
            floor=math.floor,
            hash=hash,
            int=int,
            trunc=math.trunc,
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