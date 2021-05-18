# You will be given two inputs: a string of words and a letter.
# For each string, return the alphabetic character after every instance of letter(case insensitive).
#
# If there is a number, punctuation or underscore following the letter, it should not be returned.
#
# If letter = 'r':
# comes_after("are you really learning Ruby?") # => "eenu"
# comes_after("Katy Perry is on the radio!")   # => "rya"
# comes_after("Pirates say arrrrrrrrr.")       # => "arrrrrrrr"
# comes_after("r8 your friend")                # => "i"
# Return an empty string if there are no instances of letter in the given string.

def comes_after(st, l):
    result = ''
    i = 0
    while i < len(st)-1:
        if st[i].lower() == l.lower():
            if st[i+1].isalpha():
                result += st[i+1]
        i += 1
    return result



print(comes_after("Pirates say arrrrrrrrr.", 'r'))
print(comes_after("Free coffee for all office workers!", 'F'))
print(comes_after("king kUnta is the sickest rap song ever kNown k!", 'k'))
print(comes_after("d8u d._ rly 2d1s", 'D'))

# def comes_after(st, l):
#     result = ''
#     l = l.lower()
#     print(list(zip(st.lower(), st[1:])))
#     for x, y in zip(st.lower(), st[1:]):
#         if x == l and y.isalpha():
#             result += y
#     return result
