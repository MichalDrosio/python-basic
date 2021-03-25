# Given an array of numbers (in string format), you must return a string.
# The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc.
# You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.
#
# All inputs will be valid.
import string

def switcher(arr):
    az = string.ascii_lowercase[::-1] + '!? '
    return ''.join(az[int(x)-1] for x in arr if int(x) > 0)


print(switcher(['24', '12', '23', '22','0', '4', '26', '9', '8',]))
print(switcher(['25','7','8','0','4','14','23','8','25','23','29','16','16','4']))

