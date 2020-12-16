class Vector:
    def __init__(self,*components):
        self.components = components

    def __repr__(self):
        return f'{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __bool__(self):
        if not self.components:
            return False
        elif self.components[0] != 0:
            return True

    def __add__(self, other):
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return Vector(*components)

    def __sub__(self, other):
        components = tuple(x - y for x, y in zip(self.components, other.components))
        return Vector(*components)

    def __mul__(self, other):
        components = tuple(x * y for x, y in zip(self.components, other.components))
        return Vector(*components)

    def __truediv__(self, other):
        components = tuple(x / y for x, y in zip(self.components, other.components))
        return Vector(*components)

    def __floordiv__(self, other):
        components = tuple(x // y for x, y in zip(self.components, other.components))
        return Vector(*components)




v1 = Vector(1, 2, 3)
v2 = Vector(-1, -2, 2)
v3 = Vector()
print(v1)
print(v2)
print(v2.__len__())
print(len(v1))
print(bool(v1))
print(bool(v2))
print(bool(v3))
print(f'v1+v2={v1+v2}')
print(f'v1({v1})-v2({v2})={v1-v2}')
print(f'v1({v1})*v2({v2})={v1*v2}')
print(f'v1({v1})/v2({v2})={v1/v2}')
print(f'v1({v1})//v2({v2})={v1//v2}')

