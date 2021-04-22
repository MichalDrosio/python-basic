def testit(a, b):
    # return a|b
    if a % 2 == 1 and b % 2 == 1:
        return max(a, b)
    else:
        return a + b

print(testit(1, 3))