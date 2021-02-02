# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1
# which are substrings of strings of a2.
#
# #Example 1: a1 = ["arp", "live", "strong"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns ["arp", "live", "strong"]
#
# #Example 2: a1 = ["tarp", "mice", "bull"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns []
#
# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
#
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
#
# Beware: r must be without duplicates.
# Don't mutate the inputs.

def in_array(array_1, array_2):
    result = []
    for i in array_1:
        for j in array_2:
            if i in j:
                if i not in result:
                    result.append(i)
    return sorted(result)

array_1 = ["arp", "live", "strong"]
array_2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(array_1, array_2))

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1, a2))
