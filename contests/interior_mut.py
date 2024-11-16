class InteriorMut:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.__class__.__name__}<{self.value}>'

    def __class_getitem__(cls, item):
        return cls(item)