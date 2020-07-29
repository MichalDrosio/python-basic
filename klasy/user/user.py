


class User():
    def __init__(self, name, surname, age, sex):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.login = 0

    def describe_user(self):
        print(f"uzytkownik {self.name} {self.surname}"
              f"\n\twiek:{self.age}"
              f"\n\tplec:{self.sex}")

    def greet_user(self):
        print(f'witaj {self.name} {self.surname}')

    def increment_login_attempts(self):
        self.login += 1
        print(f'zalogowano sie {self.login} razy')
    def reset_login_attempts(self):
        self.login = 0
        return f'resetowanie, aktualna wartosc:{self.login}'

up=['dodac post', 'usunac post', 'banowac']

class Admin(User):
    def __init__(self, name, surname, age, sex, privileges):
        self.privileges = privileges
        super(Admin, self).__init__(name, surname, age, sex)

    def show_privileges(self):
        print(f'Administrator {self.name} {self.surname} może: ')
        for self.privilege in self.privileges:
            print(f'\t-{self.privilege}')

user1 = User('michal', 'drosio', 33, 'm')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.reset_login_attempts())
admin = Admin(name='michal', surname='drosio', age=33, sex='m',privileges=up)
admin.show_privileges()