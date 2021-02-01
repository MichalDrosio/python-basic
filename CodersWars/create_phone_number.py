def create_phone_number(n):
    first = ''.join(str(x) for x in n[0:3])
    mid = ''.join(str(x) for x in n[3:6])
    last = ''.join(str(x) for x in n[6:10])
    return f'({first}) {mid}-{last}'



def create_phone_number2(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))