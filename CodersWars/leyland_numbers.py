# A Leyland number is a number of the form xy+yxx^y + y^xx y +y where xxx and yyy are integers greater than 1.
# The first few such numbers are:
# 8=2^2 + 2^2
# 17=2^3+3^2
# 32 = 2^4 + 4^2
# 54=3^3 = 3^3 + 3^3
# Return all Leyland numbers up to 1012 as a list, in ascending order.

# Your code can be maximum 80 characters long.

# r = range(2,40)
# f = lambda: sorted({i**j+j**i for i in r for j in r})[:121]
#
#
# def leyland(number):
#     result = {}
#
#     for num in range(2, int(number/2)):
#         for num1 in range(2, int(number / 2)):
#             if num ** num1 <= int(number/2):
#                 result[f'{num}**{num1}'] = num**num1
#     return result
#
# print(leyland(32))

def binary_gap(N):
    z = bin(N)[2:]
    print(z)
    s = z.strip('0').split('1')
    print(s)
    r = len(max(format(N, 'b').strip('0').split('1')))
    if r <1:
        return 0
    return r
print(binary_gap(1041))
def soluyion(array):
    m = max(array)
    n = min(array)
    if n >0:
        for i in range(n, m):
            if i not in array:
                return i

        return m+1
    return 1
print(soluyion([-1,-3]))