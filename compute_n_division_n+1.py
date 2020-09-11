# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).


def compute(num):
    z = 0
    for i in range(1, num+1):
        z += float(i) / (i+1)
    return round(z, 2)


while True:
    try:
        print(compute(num=int(input('liczba'))))
    except ValueError:
        print('podaj liczbe')
