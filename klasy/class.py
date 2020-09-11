# Define a class, which have a class parameter and have a same instance parameter.


class Person:
    name = 'Ola'

    def __init__(self, name=None):
        self.name = name

p = Person('Aleksandra')
print(f'{Person.name} is {p.name}')