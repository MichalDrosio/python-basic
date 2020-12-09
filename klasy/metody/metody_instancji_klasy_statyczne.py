class Employee:
    EMPLOYEES_GRADES = {
        'A': '2500',
        'B': '3000',
        'C': '3500',
        'D': '4000'
    }

    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = surname

        if grade not in Employee.EMPLOYEES_GRADES:
            raise ValueError(f'Wrong employee grade. Available grades: {list(Employee.EMPLOYEES_GRADES)}')
        self.grade = Employee.EMPLOYEES_GRADES[grade]
        # self.grade = self.EMPLOYEES_GRADES[grade]

    def show_employee_info(self):
        print(f'Name: {self.name} {self.surname}. Salary: {self.grade}')

    def show_grade(self):
        for grade, salary in Employee.EMPLOYEES_GRADES.items():
            print(f'{grade} - {salary}')

    @classmethod
    def add_grade(cls, grade, salary):
        cls.EMPLOYEES_GRADES[grade] = salary

    @classmethod
    def create_from_string(cls, text):
        name, surname, grade = text.split(";")
        return cls(name, surname, grade)

    @staticmethod
    def who_is_your_manager():
        print('The menager is Maja Drosio')


e1 = Employee('Ola', 'Woznica', 'D')
e1.show_employee_info()
e1.show_grade()
Employee.add_grade('E', 4500)
e1.show_grade()
e2 = Employee.create_from_string('Magda;Trojanowska;B')
e2.show_employee_info()
Employee.who_is_your_manager()
e1.who_is_your_manager()