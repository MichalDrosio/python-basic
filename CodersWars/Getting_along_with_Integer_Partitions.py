
def stringy(size):
    res = ''
    for i in range(size):
        if i % 2 == 0:
           res += '1'
        else:
            res += '0'
    return res

print(stringy(6))



