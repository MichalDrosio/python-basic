# Consider the prime number 23.
# If we sum the square of its digits we get: 2^2 + 3^2 = 13, then for 13: 1^2 + 3^2 = 10,
# and finally for 10: 1^2 + 0^2 = 1.
#
# Similarly, if we start with prime number 7, the sequence is: 7->49->97->130->10->1.
#
# Given a range, how many primes within that range will eventually end up being 1?
#
# The upperbound for the range is 50,000. A range of (2,25) means that: 2 <= n < 25.


def is_prime(number):
    if number < 2:
        return False
    for num in range(2, int(number**0.5)+1):
        if number % num == 0:
            return False
    return True


def solve(a, b):
    result = 0
    for num in range(a, b):
        if is_prime(num):
            x = 0
            while num != 1 and x != 10:
                num = sum(int(i)**2 for i in list(str(num)))
                x += 1
            if num == 1:
                result += 1
    return result


print(solve(100, 1000))