# Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down),
# these numbers remain the same. To clarify, if we write them down on a paper and turn the paper upside down,
# the numbers will be the same. Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.
#
# Given a range, return the count of upside down numbers within that range.
# For example, solve(0,10) = 3,
# because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.
#
# More examples in the test cases.

def solve(a, b):
    numbers = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6"
    }
    result = 0
    for i in range(a, b):
        if i < 10:
            if i in (0, 1, 8):
                result += 1
        elif i > 9:
            num = str(i)
            new = ''
            j = 0
            while j < len(num):
                if num[j] not in numbers:
                    break
                else:
                    new += numbers[num[j]]
                j += 1
                if new[::-1] == num:
                    print(num, new[::-1])
                    result += 1

    return result


print(solve(1000, 10000))