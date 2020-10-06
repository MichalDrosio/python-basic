import math


def check_prime_number(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def gen_primary_number(num):
    for i in range(2, num+1):
        if check_prime_number(i):
            yield i


print(list(gen_primary_number(100)))

