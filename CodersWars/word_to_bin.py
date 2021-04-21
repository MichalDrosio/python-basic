def word_to_bin(word):
    l = []
    n = '0'
    for i in word:
        z = ord(i)
        b = bin(z)[2:]
        if len(b) < 8:
            c = 8 - len(b)
            x = n*c + b
            l.append(x)
        else:
            l.append(b)
    return l

print(word_to_bin('man'))