# A Narcissistic Number is a number of length n in which the sum of its digits to
# the power of n is equal to the original number. If this seems confusing, refer to the example below.
#
# Ex: 153, where n = 3 (number of digits in 153)
# 13 + 53 + 33 = 153
#
# Write a method is_narcissistic(i) (in Haskell: isNarcissistic :: Integer -> Bool)
# which returns whether or not i is a Narcissistic Number.

def is_narcissistic(i):
    i_str = str(i)
    c = 0
    for x in i_str:
        c += int(x)**len(i_str)
        if c > i:
            return False
    if c == i:
        return True
    return False
print(is_narcissistic(153))
print(is_narcissistic(201))