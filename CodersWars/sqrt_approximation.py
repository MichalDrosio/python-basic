# We want to approximate the sqrt function. Usually this function takes a
# floating point number and returns another floating point number,
# but in this kata we're going to work with integral numbers instead.
#
# Your task is to write a function that takes an integer n and returns either
#
# an integer k if n is a square number, such that k * k == n or
# a range (k, k+1), such that k * k < n and n < (k+1) * (k+1).
# Examples
# sqrt_approximation(4) --> 2
# sqrt_approximation(5) --> [2,3]
# Note : pow() and sqrt() functions are disabled.




def sqrt_approximation(number):
    for i in range(int(number/2)+1, 1, -1):
        print(f'{i}*{i}=={i*i}')
        if i * i == number:
            return i
        else:
            if i * i < number:
                return [i, i+1]


print(sqrt_approximation(85))