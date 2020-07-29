class Employee():
    def __init__(self, name, surname, year_income):
        self.name = name
        self.surname = surname
        self.year_income = year_income

    def give_raise(self, amount=5000):
        self.year_income += amount
        return self.year_income

employee =Employee('michal', 'drosio',200000)

