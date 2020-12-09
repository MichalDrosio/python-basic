class Employee:
    quantity_employee = 0

    def __init__(self, name, surname, email, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.salary = salary
        Employee.quantity_employee += 1

    def get_annual_salary(self):
        if self.salary > 0:
            return self.salary * 12

    def show_employee_information(self):
        print(f"{self.name} {self.surname}, {self.email} ma pensje {self.salary}")