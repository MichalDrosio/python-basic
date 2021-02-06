# To participate in a prize draw each one gives his/her firstname.
#
# Each letter of a firstname has a value which is its rank in the English alphabet.
# A and a have rank 1, B and b rank 2 and so on.
#
# The length of the firstname is added to the sum of these ranks hence a number som.
#
# An array of random weights is linked to the firstnames and each som is multiplied
# by its corresponding weight to get what they call a winning number.
#
# Example:
# names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
# weights: [1, 4, 4, 5, 2, 1]
#
# PauL -> som = length of firstname + 16 + 1 + 21 + 12 = 4 + 50 -> 54
# The *weight* associated with PauL is 2 so PauL's *winning number* is 54 * 2 = 108.
# Now one can sort the firstnames in decreasing order of the winning numbers.
# When two people have the same winning number sort them alphabetically by their firstnames.
#
# Task:
# parameters: st a string of firstnames, we an array of weights, n a rank
#
# return: the firstname of the participant whose rank is n (ranks are numbered from 1)
#
# Example:
# names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
# weights: [1, 4, 4, 5, 2, 1]
# n: 4
#
# The function should return: "PauL"
import string


def count_weights(name):
    num = 0
    for weight, letter in enumerate(string.ascii_lowercase):
        if letter in name.lower():
            num += (weight+1)
    l_name = len(name)
    return num + l_name





def rank(names, weights, n):
    result = {}
    print(weights)
    names = names.split(',')
    for i in names:
        print(count_weights(i))
        result[i] = count_weights(i) * n
    sort = sorted(result.items(), key=lambda x: (-x[1], x[0]))
    return [name for name, som in sort][n - 1]




names = "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
weights = [1, 4, 4, 5, 2, 1]
n = 4

print(rank(names, weights, 2))

