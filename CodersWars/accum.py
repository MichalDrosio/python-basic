# This time no story, no theory.
# The examples below show you how to write function accum:
#
# Examples:
#
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"



def accum(s):
    new = []
    for i in range(len(s)):
        new.append(i * s[i] + s[i])
    new_str = '-'.join(new)
    return new_str.title()

print(accum('abcd'))


def accum2(s):
    return '-'.join([c.upper() + c.lower() * i for i, c in enumerate(s)])

print(accum2('abcd'))


def accum3(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))