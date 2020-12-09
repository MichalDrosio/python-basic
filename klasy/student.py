class Student:

    discount_for_shopping = 50

    def __init__(self, name, surname, no_of_index):
        self.__name = name
        self.__surname = surname
        self.no_of_index = no_of_index

    def do_you_like_studying(self):
        print("I don't know")

    def introduce_yourself(self):
        print(f"My name is {self.__name} {self.__surname}")

    def change_surname(self, surname):
        self.__surname = surname


class GoodStudent(Student):
    def __init__(self, name, surname,  no_of_index, scholarship):
        super(GoodStudent, self).__init__(name, surname, no_of_index)
        self.scholarship = scholarship

    def do_you_like_studying(self):
        print("Rather yes")


class BadStudent(Student):
    def __init__(self, name, surname,  no_of_index, current_repeatable_year):
        super(BadStudent, self).__init__(name, surname, no_of_index)
        self.current_repeatable_year = current_repeatable_year

    def do_you_like_studying(self):
        Student.do_you_like_studying(self)
        print("I don't like")

# s = Student('Ola', 'Drosio', 1)
# s.introduce_yourself()
# print(f'{s.no_of_index}')
# s.__surname = 'Woznica'

l = []
l.append(GoodStudent("Ola", "Woznica", 2, 1500))
l.append(BadStudent("Maciek", "Kowalski", 5, 4))
for s in l:
    s.do_you_like_studying()