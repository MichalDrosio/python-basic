class Animal:
    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age

    def print_welcome(self):
        print(f'Jestem {self.name} i mam {self.age}')
        
class Dog(Animal):
    def __init__(self, name, age):
        super(Dog, self).__init__(name, age)

    def show_goodbye(self):
        print(f'{self.name} zegna')

x = Animal('Nala', 2)
y = Dog('Red', 10)

print(x.name, x.age)
print(y.name, y.age)

print(isinstance(x,Animal))
print(isinstance(x,Dog))
x.print_welcome()
y.print_welcome()
y.show_goodbye()