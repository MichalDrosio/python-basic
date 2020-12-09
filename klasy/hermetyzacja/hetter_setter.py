class BankAccount:
    def __init__(self, name, surname, initial_balance):
        self.name = name
        self.surname = surname
        self._balance = initial_balance

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Negative amount is not allowed")
        self._balance = value

account_1 = BankAccount('Ola', 'Woznica', 1000)
print(account_1.balance)
account_1.balance = 100
print((account_1.balance))