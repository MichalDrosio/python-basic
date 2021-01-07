n = 1
pv = 1000
r = 0.04
fv = pv * (1 + r)

while fv <= 2000:
    fv *= (1 + r)
    n += 1
print(f'{fv:.2f}, {n}')
