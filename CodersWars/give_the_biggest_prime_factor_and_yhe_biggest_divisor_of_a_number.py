# Given a certain integer n, we need a function big_primefac_div(),
# that give an array with the highest prime factor and the highest divisor (not equal to n).
#
# Let's see some cases:
#
# big_primefac_div(100) == [5, 50]
# big_primefac_div(1969) == [179, 179]
# If n is a prime number the function will output an empty list:
#
# big_primefac_div(997) == []
# If n is an negative integer number, it should be considered the division with tha absolute number of the value.
#
# big_primefac_div(-1800) == [5, 900]
# If n is a float type, will be rejected if it has a decimal part with some digits different than 0.
# The output "The number has a decimal part. No Results".
# But n will be converted automatically to an integer if all the digits of the decimal part are 0.
import math


def max_div_num(number):
    for num in range(int((number/2)+1), 1, -1):
        if number % num == 0:
            return num


def is_prime(number):
    for num in range(2, int(math.sqrt(number)+1)):
        if number % num == 0:
            return False
    return True


def big_primefac_div(number):
    number = abs(number)
    if number % 1 != 0:
        return "The number has a decimal part. No Results"
    elif is_prime(number):
        return []
    else:
        div = max_div_num(number)
        for num in range(div, 2, -1):
            if is_prime(num) and number % num == 0:
                return [num, div]


print(big_primefac_div(983434))

