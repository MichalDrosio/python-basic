def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


print(factorial(10))


def factorial_2(num):
    if num == 0:
        return 1
    return num * factorial(num-1)


print(factorial(10))