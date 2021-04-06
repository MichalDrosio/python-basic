# Given a string of words, you need to find the highest scoring word.
#
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#
# You need to return the highest scoring word as a string.
#
# If two words score the same, return the word that appears earliest in the original string.
#
# All letters will be lowercase and all inputs will be valid.

import string

def high(txt):
    z = string.ascii_lowercase
    res = 0
    longest_word = ''
    for word in txt.split(' '):
        r = 0
        for w in word:
            r += z.index(w) + 1

        if res < r:
            res = r
            longest_word = word

    return longest_word

print(high('cd i ab michal ola xxx'))

