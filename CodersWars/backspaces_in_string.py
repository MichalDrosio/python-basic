# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
#
# Your task is to process a string with "#" symbols.
#
# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""

def clean_string(s):
    arr = []
    for a in s:
        if a != '#':
            arr.append(a)
        elif arr:
            arr.pop()
    if arr:
        return ''.join(arr)
    else:
        return ''

print(clean_string('abc###d##c'))
print(clean_string('#########'))