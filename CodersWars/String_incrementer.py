def increment_string(strng):
    stripped = strng.rstrip('1234567890')
    ints = strng[len(stripped):]
    if len(ints) == 0:
        return strng + '1'
    else:
        length = len(ints)
        new_ints = 1 + int(ints)
        nli = length - len(str(new_ints))
        if length != nli:
            return stripped + '0'*nli + str(new_ints)

        return stripped + new_ints

print(increment_string('a321dsa009'))