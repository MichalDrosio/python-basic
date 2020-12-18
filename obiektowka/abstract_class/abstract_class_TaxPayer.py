from abc import ABC, abstractmethod


class TaxPayer(ABC):
    def __init__(self, salary):
        self.salary = salary

    @abstractmethod
    def calculate_tax(self):
        pass


class StudentTaxPayer(TaxPayer):
    def __init__(self, salary):
        super(StudentTaxPayer, self).__init__(salary)

    def calculate_tax(self):
        return self.salary * 0.15


class DisabledTaxPayer(TaxPayer):
    def __init__(self, salary):
        super(DisabledTaxPayer, self).__init__(salary)

    def calculate_tax(self):
        return self.salary * 0.12


class WorkerTaxPayer(TaxPayer):
    def __init__(self, salary):
        super(WorkerTaxPayer, self).__init__(salary)

    def calculate_tax(self):
        if self.salary < 80000:
            return self.salary * 0.17
        else:
            return 80000 * 0.17 + (self.salary - 80000) * 0.32


stp = StudentTaxPayer(40000)
print(stp.calculate_tax())
disabled = DisabledTaxPayer(50000.0)
print(disabled.calculate_tax())
worker_tax = WorkerTaxPayer(70000)
worker_tax_2 = WorkerTaxPayer(95000)
print(worker_tax.calculate_tax())
print(worker_tax_2.calculate_tax())
print('-'*100)
tax_payers = [StudentTaxPayer(50000), DisabledTaxPayer(70000), WorkerTaxPayer(68000), WorkerTaxPayer(120000)]
for tax in tax_payers:
    print(tax.calculate_tax())