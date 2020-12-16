class Person:
    instances = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Person.instances.append(self)

    @classmethod
    def show_details(cls):
        print(f'Running from {cls.__name__} class')

    @classmethod
    def count_instances(cls):
        return len(Person.instances)


person = Person('Ola', 'Kowalczyk')
person.show_details()
p1 = Person('Jan', 'Wójcik')
p2 = Person('Magda', 'Lem')
p3 = Person('Robert', 'Kruk')
print(Person.count_instances())