class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def set_first_name(self, name):
        self._first_name = name

    def set_last_name(self, surname):
        self._last_name = surname

    def del_first_name(self):
        del self._first_name

    first_name = property(fget=get_first_name, fset=set_first_name, fdel=del_first_name)
    last_name = property(fget=get_last_name, fset=set_last_name)


person = Person('John', 'Dow')
print(person.get_first_name())
print(person.get_last_name())
print(person.first_name)
print(person.last_name)
print(person.__dict__)
person.set_first_name('Mike')
print(person.get_first_name())
print(person.first_name)
person.set_last_name('Smith')
print(person.last_name)
print(person.get_first_name())

print(person.__dict__)
person.del_first_name()
print(person.__dict__)