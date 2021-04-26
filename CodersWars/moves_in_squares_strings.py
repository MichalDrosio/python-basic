# You are given a string of n lines, each substring being n characters long: For example:
#
# s = "abcd\nefgh\nijkl\nmnop"
#
# We will study some transformations of this square of strings.
#
# Clock rotation 180 degrees: rot
# rot(s) => "ponm\nlkji\nhgfe\ndcba"
# selfie_and_rot(s) (or selfieAndRot or selfie-and-rot) It is initial string + string obtained by clock rotation
# 180 degrees with dots interspersed in order (hopefully) to better show the rotation when printed.
# s = "abcd\nefgh\nijkl\nmnop" -->
# "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"
# or printed:
# |rotation        |selfie_and_rot
# |abcd --> ponm   |abcd --> abcd....
# |efgh     lkji   |efgh     efgh....
# |ijkl     hgfe   |ijkl     ijkl....
# |mnop     dcba   |mnop     mnop....
#                            ....ponm
#                            ....lkji
#                            ....hgfe
#                            ....dcba
# Notice that the number of dots is the common length of "abcd", "efgh", "ijkl", "mnop".
#
# Task:
# Write these two functions rotand selfie_and_rot
# and
#
# high-order function oper(fct, s) where
#
# fct is the function of one variable f to apply to the string s (fct will be one of rot, selfie_and_rot)
#
# Examples:
# s = "abcd\nefgh\nijkl\nmnop"
# oper(rot, s) => "ponm\nlkji\nhgfe\ndcba"
# oper(selfie_and_rot, s) => "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....

def rot(strng):
    return strng[::-1]

def selfie_and_rot(strng):
    s = strng.split()
    s_r = rot(strng).split()
    z = '.'*len(s)
    x = f'{z}\n'.join(s)
    y = f'\n{z}'.join(s_r)
    return f'{x}{z}\n{z}{y}'


def oper(fct, s):
    return fct(s)



# print(rot("abcd\nefgh\nijkl\nmnop"))
#
# print(selfie_and_rot(("abcd\nefgh\nijkl\nmnop")))

print(oper(rot, "rkKv\ncofM\nzXkh\nflCB"))
print(oper(selfie_and_rot, "xZBV\njsbS\nJcpN\nfVnP"))