class Imaginary:
    __slots__ = ('x', 'y')

    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "{} + {}i".format(self.x, self.y)

    def __hash__(self):
        return hash(self.x, self.y)

    def __add__(self, other):
        return Imaginary(self.x + other.x, self.y + other.y)

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return self


img = Imaginary
a = img(1, 1)
b = img(2)

c = a + b

args = [1, 2, 3]
kwargs = {'first': 'a', 'second': 'b'}

a(*args, **kwargs)
