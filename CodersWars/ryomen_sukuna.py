# Ryomen Sukuna has entered your body, and he will only leave if you can solve this problem.
#
# Given an integer n, how many integers between 1 and n (inclusive) are unrepresentable as aba^ba
# b
#  , where aaa and bbb are integers not less than 2?
#
# Example:
#
# if n equals 10 then output must be 7,
# as 4 is representable as 22, 8 as 23 and 9 as 32.
# So the numbers left are 1, 2, 3, 5, 6, 7 and 10.
#
# Note:
#
# Optimize your solution for n as large as 1010.

def sukuna(n):
    res = []
    i = 2
    while i * i <= n:
        z = i*i
        print(f'{i}*{i}=={z}')
        while z <= n:
            res.insert(-1, z)
            print(res)
            print(f'{i}*{z}=={z * i}')
            z *= i
        i += 1
    return n - len(sorted(res))


print(sukuna(10))
