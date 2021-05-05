# You will be given a string with sets of characters, (i.e. words),
# seperated by between one and three spaces (inclusive).
#
# Looking at the first letter of each word (case insensitive-"A" and "a" should be treated the same),
# you need to determine whether it falls into the positive/first half of the alphabet ("a"-"m")
# or the negative/second half ("n"-"z").
#
# Return True if there are more (or equal) positive words than negative words, False otherwise.
#
# "A big brown fox caught a bad rabbit" => True
# "Xylophones can obtain Xenon." => False
import string

def connotation(strng):
    letters = string.ascii_lowercase
    strng = strng.lower().split()
    b = letters.index('n')
    p = 0
    n = 0
    for i in strng:
        if i[0] in letters[:b]:
            p += 1
        else:
            n += 1
    if p >= n:
        return True
    else:
        return False

print(connotation("CHOCOLATE MAKES A GREAT SNACK"))