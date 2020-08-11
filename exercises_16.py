# Konwersja liczby dziesietnej na binarną

def bin(a,b):
    c = a + b

    binarna = []
    while c > 0:
        if c % 2 == 0:
            binarna.append('0')
        if c % 2 != 0:
            binarna.append('1')
        c = (c / 2) - ((c % 2) / 2)
    x = binarna[::-1]
    return ''.join(x)

print(bin(10,10))
