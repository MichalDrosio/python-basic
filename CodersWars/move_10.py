# Move every letter in the provided string forward 10 letters through the alphabet.
#
# If it goes past 'z', start again at 'a'.
#
# Input will be a string with length > 0
import string


def move_ten(word):
    new_word = ''
    letters = string.ascii_lowercase
    for l in word:
        new_letter = letters.index(l) + 10
        if new_letter <= 26:
            new_word += letters[new_letter]
        else:
            new_letter = new_letter - 26
            new_word += letters[new_letter]
    return new_word


print(move_ten('exp'))

from string import ascii_lowercase as al

tbl = str.maketrans(al, al[10:] + al[:10])
def move_ten2(st):
    return st.translate(tbl)

print(move_ten2('exp'))