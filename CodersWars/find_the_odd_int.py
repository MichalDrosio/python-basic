# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]


def find_it_2(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


print(find_it([1,1,3,3,3,3,3,5,5,5,5,5,5]))
print(find_it_2([1,1,3,3,3,3,3,5,5,5,5,5,5]))




