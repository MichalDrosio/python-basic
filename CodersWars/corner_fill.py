# Corner Fill
# You receive a two dimensional array of size n x n and you want to
# fill in the square in one stroke while starting from 0:0 and ending on n-1:0.
#
# If n = 3 then:
#
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# Starting from left to right and then top to bottom we can grab the first corner!
# We then return on the inside of this corner to get the next one, and so on (see image below).

def corner_fill(square):
    array = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
    col = int(square[0])
    row = int(square[2])
    result = []
    for i in array[:col]:
        for j in i[:row]:
            result.append(j)
    return result
print(corner_fill('3x3'))

