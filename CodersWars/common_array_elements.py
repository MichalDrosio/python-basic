# Given three arrays of integers,
# return the sum of elements that are common in all three arrays.
#
# For example:
#
# common([1,2,3],[5,3,2],[7,3,2]) = 5 because 2 & 3 are common in all 3 arrays
# common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays

def common(a, b, c):
    num = 0
    for i in a:
        if i in b and i in c:
            num += i
    return num


# print(common([1,2,3],[5,3,2],[7,3,2]))
# print(common([1,2,2,3],[5,3,2,2],[7,3,2,2]))

def common2(a,b,c):
    a.sort() ; b.sort() ; c.sort()
    i = j = k = c1 = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] == c[k]:
            c1 += a[i]
            i += 1 ; j += 1 ; k += 1
        elif a[i] < b[j] : i += 1
        elif b[j] < c[k] : j += 1
        else : k += 1
    return c1

print(common2([1,2,3],[5,3,2],[7,3,2]))
print(common2([1,2,2,3],[5,3,2,2],[7,3,2,2]))