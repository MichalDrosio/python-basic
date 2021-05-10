# There are some stones on Bob's table in a row, and each of them can be red, green or blue,
# indicated by the characters R, G, and B.
#
# Help Bob find the minimum number of stones he needs to remove from the
# table so that the stones in each pair of adjacent stones have different colours.
#
# Examples:
#
# "RGBRGBRGGB"   => 1
# "RGGRGBBRGRR"  => 3
# "RRRRGGGGBBBB" => 9

# def solution(stones):
#     count = 0
#     for i in range(1, len(stones)):
#         if stones[i-1] == stones[i]:
#             count += 1
#     return count

def solution(stones):
    print(len(stones))
    i = 0
    c = 0
    while i < len(stones)-1:
        print(stones[i], stones[i+1])
        if stones[i] == stones[i+1]:
            c += 1
        i += 1
    return c



print(solution('RGBRGBRGGB'))