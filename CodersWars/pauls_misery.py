def paul(x):
    points = {'life': 0, 'eating': 1, 'kata': 5, 'Petes kata': 10}
    misery = sum(map(points.get, x))
    return ['Miserable!', 'Sad!', 'Happy!', 'Super happy!']\
            [(misery<40)+(misery<70)+(misery<100)]



def paul2(x):
    d = {'kata': 5, 'Petes kata': 10, 'life': 0, 'eating': 1}
    z = 0
    for i in x:
        z += d[i]
    if z > 100:
        res = 'Miserable!'
    elif z >= 70:
        res = 'Sad!'
    elif z >= 40:
        res = 'Happy!'
    else:
        res = 'Super happy!'
    return res





s =['life', 'eating', 'life']
print(paul(s))


