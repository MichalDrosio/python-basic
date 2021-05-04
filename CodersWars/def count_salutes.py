# There is a narrow hallway in which people can go right and left only.
# When two people meet in the hallway, by tradition they must salute each other.
# People move at the same speed left and right.
#
# Your task is to write a function that, given a string representation of people moving in the hallway,
# will count the number of salutes that will occur.
# Note: 2 salutes occur when people meet, one to the other and vice versa.

# People moving right will be represented by >; people moving left will be represented by <.
# An example input would be >--<--->->. The - character represents empty space, which you need not worry about.

# Input: >----->-----<--<
# Output: 8
#
# Explanation: Both guys moving right will meet both guys moving left.
# Hence a total of 4 meetings will occur and 8 salutes will occur.
#
# Input: <---<--->----<
# Output: 2
#
# Explanation: Only one meeting occurs.

def count_salutes(hallway):
    salutes = 0
    for index, c in enumerate(hallway):
        if c == ">":
            print(index, c, 2 * hallway[index:].count("<"))
            salutes += 2 * hallway[index:].count("<")
    return salutes


print(count_salutes('>--->---<--<'))