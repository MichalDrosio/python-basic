# The goal of this Kata is to write a function that will receive an array of strings as its single argument,
# then the strings are each processed and sorted (in desending order)
# based on the length of the single longest sub-string of contiguous vowels ( aeiouAEIOU )
# that may be contained within the string. The strings may contain letters, numbers, special characters,
# uppercase, lowercase, whitespace, and there may be (often will be) multiple sub-strings of contiguous vowels.
# We are only interested in the single longest sub-string of vowels within each string, in the input array.
#
# Example:
#
# str1 = "what a beautiful day today"
# str2 = "it's okay, but very breezy"
# When the strings are sorted, str1 will be first as its longest sub-string of contiguous vowels "eau"
# is of length 3, while str2 has as its longest sub-string of contiguous vowels "ee", which is of length 2.
#
# If two or more strings in the array have maximum sub-strings of the same length,
# then the strings should remain in the order in which they were found in the orginal array.


def sort_strings_by_vowels(seq):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    vp = []
    out = []

    count, res = 0, 0

    for st in seq:

        for i in range(len(st)):

            if st[i] in vowels:

                count += 1

            else:

                res = max(res, count)  # compare two value and store the max to res

                count = 0

        vowel_ct = max(res, count)
        vp.append((st, vowel_ct))
        res, count = 0, 0

    sort_vp = sorted(vp, key=lambda x: x[1], reverse=True)

    for i in sort_vp:
        out.append(i[0])

    return (out)


print(sort_strings_by_vowels(["aa","eee","oo","iiii"]))