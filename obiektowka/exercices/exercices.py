class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        return f'{self.name}->{self.age}'


people = [Person('Tom', 25), Person('John', 29),
          Person('Mike', 27), Person('Alice', 19)]

people.sort(key=lambda person: person.age)

for person in people:
    print(person.show_person())