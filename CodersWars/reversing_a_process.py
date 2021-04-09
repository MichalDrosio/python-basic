# Suppose we know the process by which a string s was encoded to a string r (see explanation below).
# The aim of the kata is to decode this string r to get back the original string s.
#
# Explanation of the encoding process:
# input: a string s composed of lowercase letters from "a" to "z", and a positive integer num
# we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ...
# if c is a character of s whose corresponding number is x, apply to x the function f: x-> f(x) = num * x % 26,
# then find ch the corresponding character of f(x)
# Accumulate all these ch in a string r
# concatenate num and r and return the result
# For example:
#
# encode("mer", 6015)  -->  "6015ekx"
#
# m --> 12,   12 * 6015 % 26 = 4,    4  --> e
# e --> 4,     4 * 6015 % 26 = 10,   10 --> k
# r --> 17,   17 * 6015 % 26 = 23,   23 --> x
#
# So we get "ekx", hence the output is "6015ekx"
def decode(r):
    abc='abcdefghijklmnopqrstuvwxyz'
    for i in range(len(r)):
        if r[i].isalpha():
            num=r[:i]
            s=r[i:]
            break
    nums=[x*int(''.join(num))%26 for x in range(26)]
    if len(set(nums))!=len(nums):
        return 'Impossible to decode'
    snums=[abc.index(str(i)) for i in s]
    s=[abc[nums.index(a)] for a in snums]
    return ''.join(s)


print(decode('6015ekx'))
# print(decode('5057aan'))



