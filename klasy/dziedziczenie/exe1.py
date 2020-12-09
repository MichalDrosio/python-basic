class Teacher:
    def __init__(self, name, surname, number_of_students):
        self.name = name
        self.surname = surname
        self.number_of_students = number_of_students

    def show_info(self):
        print(f'{self.name} {self.surname} - {self.number_of_students} uczniów')


t = Teacher("Magda", "Kowalska", 25)
t.show_info()


class MathematicsTeacher(Teacher):
    pass

t1 = MathematicsTeacher('a', 'b', 10)
t1.show_info()
print(help(t1))