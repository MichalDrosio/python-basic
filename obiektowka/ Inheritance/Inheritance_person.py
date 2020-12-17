class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Departament:
    def __init__(self, dept_name, short_dept_name):
        self.dept_name = dept_name
        self.short_dept_name = short_dept_name


class Worker(Person, Departament):
    def __init__(self, first_name, last_name, age, dept_name, short_dept_name):
        Person.__init__(self, first_name, last_name, age)
        Departament.__init__(self, dept_name, short_dept_name)


person = Person('John', 'Doe', 35)
departament = Departament('Information Technology', 'IT')
print(person.__dict__)
print(departament.__dict__)
worker = Worker(first_name='John', last_name='Doe', age=30, dept_name='Information Technology', short_dept_name='IT')
print(worker.__dict__)
print(Worker.mro())

