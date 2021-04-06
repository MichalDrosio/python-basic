# In this Kata you will be given an array (or another language-appropriate collection) representing contestant ranks.
# You must eliminate contestant in series of rounds comparing consecutive pairs of ranks and store all initial
# and intermediate results in an array.
#
# During one round, the lowest rank of a pair is eliminated while the highest proceeds to the next round.
# This goes on until one contestant only is left. If the number of contestants is odd,
# the last one of the current array becomes the first of the next round.
#
# At the end of the competition, return the results of all the rounds in the form of array of arrays:
#
# inp = [9, 5, 4, 7, 6, 3, 8, 2]
#
# tourney(inp) == [
#   [9, 5, 4, 7, 6, 3, 8, 2],  # first round is initial input
#   [9, 7, 6, 8],              # results of 9 vs 5, 4 vs 7, 6 vs 3, and 8 vs 2
#   [9, 8],                    # results of 9 vs 7 and 6 vs 8
#   [9]                        # results of 9 vs 8
# ]
# With an odd length:
#
# input = [9, 5, 4, 7, 6, 3, 8]
# tourney(input) == [
#   [9, 5, 4, 7, 6, 3, 8],
#   [8, 9, 7, 6],           # 8 is now first because it was last in the former round
#   [9, 7],
#   [9]
# ]

def tourney(inp):
    list = inp[:]
    list2 = [inp]
    list3 = []
    while len(list) != 1:
        for i in range(len(list)):
            if i % 2 != 0:
                if list[i] >= list[i - 1]:
                    list3.append(list[i])
                else:
                    list3.append(list[i - 1])
        if len(list) % 2 != 0:
            list3.insert(0, list[-1])
        list2.append(list3)
        list = list2[-1]
        list3 = []
    return list2


def tourney2(inp):
    res = [inp]
    temp = []
    while len(inp) > 1:
        for i in range(0, len(inp), 2):
            if i + 1 == len(inp):
                temp.insert(0, inp[i])
            else:
                temp.append(max(inp[i], inp[i + 1]))
        inp = temp
        res.append(temp)
        temp = []
    return res


inp = [9, 5, 4, 7, 6, 3, 8, 2]
print(tourney2(inp))

