class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name.title()} siedzi')

    def roll_over(self):
        print(f'{self.name.title()} lezy')

d = Dog("rex", 12)
print(d.sit())
print(d.roll_over())