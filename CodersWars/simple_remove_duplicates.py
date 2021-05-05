# In this Kata, you will remove the left-most duplicates from a list of integers and return the result.
#
# # Remove the 3's at indices 0 and 3
# # followed by removing a 4 at index 1
# solve([3, 4, 4, 3, 6, 3]) # => [4, 6, 3]

def solve(arr):
    return list(set(arr))

def solve2(arr):
    res = []
    for x in arr[::-1]:
        if x not in res:
            res.append(x)
    return res[::-1]

print(solve2([3, 4, 4, 3, 6, 3]))
print(solve([1,2,1,2,1,2,3]))
print(solve([1,1,4,5,1,2,1]))