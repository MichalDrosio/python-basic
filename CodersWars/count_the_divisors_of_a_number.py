# Count the number of divisors of a positive integer n.
#
# Random tests go up to n = 500000.
#
# Examples
# divisors(4)  == 3  # 1, 2, 4
# divisors(5)  == 2  # 1, 5
# divisors(12) == 6  # 1, 2, 3, 4, 6, 12
# divisors(30) == 8  # 1, 2, 3, 5, 6, 10, 15, 30
def divisors(number):
    res = 1
    num = number // 2
    for n in range(1, num+1):
        if number % n == 0:
            res += 1
    return res

print(divisors(30))
print(divisors(12))
print(divisors(500000))