# A list S will be given. You need to generate a list T from it by following the given process:
#
# Remove the first and last element from the list S and add them to the list T.
# Reverse the list S
# Repeat the process until list S gets emptied.
# Example
# S = [1,2,3,4,5,6]
# T = []
#
# S = [2,3,4,5] => [5,4,3,2]
# T = [1,6]
#
# S = [4,3] => [3,4]
# T = [1,6,5,2]
#
# S = []
# T = [1,6,5,2,3,4]
# return T


def arrange(s):
    x = s.copy()
    T = []
    i = 0
    j = len(s)-1
    if len(s) < 2:
        return s
    else:
        while i < int(len(s)/2):
            T.append(x[i])
            T.append(x[j])
            i += 1
            j -= 1
            x = x[::-1]

        if len(s) % 2 != 0:
            mid = int(len(s)/2)
            T.append(s[mid])
            return T
        else:
            return T


S = [2, 4, 3, 4]

print(arrange(S))

def v(p):
    p = p[::-1]
    print([len(p)//2])

print(v([2,4,3,4]))