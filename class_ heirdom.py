# Define a class Person and its two child classes: Male and Female. All classes
# have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person:
    def __init__(self, sex):
        self.sex = sex

    def get_gender(self):
        return self.sex

    def name(self, name):
        return name


class Male(Person):
    def __init__(self, sex):
        super(Male, self).__init__(sex)


class Female(Person):
    def __init__(self, sex):
        super(Female, self).__init__(sex)


person = Person('Unknown')
print(person.get_gender(), person.name('Unknown'))

male = Male('Male')
print(male.get_gender(), male.name('Michal'))

female = Female('Female')
print(female.get_gender(), female.name('Ola'))


