# Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764.
# The sum of the squared divisors is 2500 which is 50 * 50, a square!
#
# Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors
# is itself a square. 42 is such a number.
#
# The result will be an array of arrays or of tuples (in C an array of Pair) or a string,
# each subarray having two elements, first the number whose squared
# divisors is a square and then the sum of the squared divisors.
def divisors(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i**2)
    return sum(result)


print(divisors(100))


def list_squared(start, end):
    result = []
    for number in range(start, end+1):
        factor = divisors(number)
        print(f'{factor**0.5}---{number}')
        if (factor**0.5).is_integer():
            print(f'{factor**0.5}-----{number}')
            result.append([number, factor])

    return result



print(list_squared(1, 100))
