def phone_number(selfphone):
    if len(selfphone) != 11:
        return False
    for i in range(0, 3):
        if not selfphone[i].isdecimal():
            return False
    if selfphone[3] != '-' or selfphone[7] != '-':
        return False
    for i in range(4, 7):
        if not selfphone[i].isdecimal():
            return False
    for i in range(8, 11):
        if not selfphone[i].isdecimal():
            return False
    return selfphone

print(phone_number())