# Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.
#
# The string may contain any of the 128 ASCII characters.
# Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters.

def has_unique_chars(string):
    for i in string.upper():

        if string.count(i) > 1:
            return False
    return True


print(has_unique_chars('12abcdef1D'))

def has_unique_chars_2(s):
    return len(s) == len(set(s))

print(has_unique_chars_2('sadbasjdb'))
