# Napisz klasę MathTools mającą jedną statyczną metodę prime_factors(n), która wygeneruje wszystkie dzielniki
# podanej liczby n w kolejności numerycznej (od najmniejszego). Do tego zadania użyj w pełni metodologii TDD.
import unittest

class MathTools:

    @staticmethod
    def prime_factors(n):
        for i in range(1, n+1):
            if n % i == 0:
                yield i

c = MathTools()
for i in c.prime_factors(30):
    print(i, end=',')

