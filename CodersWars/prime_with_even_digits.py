# Find the closest prime number under a certain integer n that has the maximum possible amount of even digits.
#
# For n = 1000, the highest prime under 1000 is 887, having two even digits (8 twice)
#
# Naming f(), the function that gives that prime, the above case and others will be like the following below.
#
# f(1000) ---> 887 (even digits: 8, 8)
#
# f(1210) ---> 1201 (even digits: 2, 0)
#
# f(10000) ---> 8887
#
# f(500) ---> 487
#
# f(487) ---> 467
import math

from pip._vendor.msgpack.fallback import xrange


def prime_digit(num):
    for n in xrange(2, int(math.sqrt(num))+1):
        if num % n == 0:
            return False
    return True


# def quantity_even_num(n):
#     count = 0
#     for i in str(n):
#         if int(i) % 2 == 0:
#             count += 1
#     return count



def high_prime_digit(number):
    max_even = 0
    max_prime = 0
    for num in xrange(number-1, 3, -1):
        if len(str(num)) <= max_even+1:
            break
        if prime_digit(num):
            even = sum(d in '02468' for d in str(num))
            if even > max_even:

                max_prime = num

                max_even = even

    return max_prime



# print(high_prime_digit(1000))
# print(high_prime_digit(1210))
# print(high_prime_digit(10000))
print(high_prime_digit(500))

