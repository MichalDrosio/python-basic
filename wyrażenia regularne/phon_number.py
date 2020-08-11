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

message = 'Zadzwoń pod nr 234-123-232, 229-098-345 '
for i in range(len(message)):
    c = message[i: i+11]
    if phone_number(c):
        print(f'znaleziono: {c} ')