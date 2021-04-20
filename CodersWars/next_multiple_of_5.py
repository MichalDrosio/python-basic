# Task
# Write a function that receives a non-negative integer n ( n >= 0 ) and returns the next higher multiple of five of that number, obtained by concatenating the shortest possible binary string to the end of this number's binary representation.
#
# Examples
# 1.  next_multiple_of_five(8)
# Steps:
#
# 8 to binary == '1000'
# concatenate shortest possible string '11' to obtain '1000' + '11' == '100011'
# '100011' to decimal == 35 => the answer
# ('001' would do the job too, but '11' is the shortest string here)
#
# 2.  next_multiple_of_five(5)
# Steps:
#
# 5 to binary =='101'
# concatenate shortest possible string '0' to obtain '101' + '0' == '1010'
# '1010' to decimal == 10
# (5 is already a multiple of 5, obviously, but we're looking for the next multiple of 5)

def next_multiple_of_five(n):
    mod5 = n % 5
    add = ''
    if n == 0:
        return 5
    elif mod5 == 0:
        add = '0'
    elif mod5 == 1:
        add = '01'
    elif mod5 == 2:
        add = '1'
    elif mod5 == 3:
        add = '11'
    elif mod5 == 4:
        add = '011'
    return int(bin(n)[2:] + add, 2)

print(next_multiple_of_five(23))