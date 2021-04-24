# Given a string, turn each character into its ASCII character code and
# join them together to create a number - let's call this number total1:
#
# 'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
# Then replace any incidence of the number 7 with the number 1, and call this number 'total2':
#
# total1 = 656667
#               ^
# total2 = 656661
#               ^
# Then return the difference between the sum of the digits in total1 and total2:
#
#   (6 + 5 + 6 + 6 + 6 + 7)
# - (6 + 5 + 6 + 6 + 6 + 1)
# -------------------------
#                        6


def calc(x):
    total_1 = []
    for letter in x:
        num = ord(letter)
        for n in str(num):
            total_1.append(int(n))

    total_2 = []
    for i in total_1:
        if i == 7:
            total_2.append(1)
        else:
            total_2.append(i)

    return sum(total_1) - sum(total_2)




print(calc('ABC'))
print(calc('jfmgklf8hglbe'))
print(calc('aaaaaddddr'))