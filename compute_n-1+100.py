# Write a program to compute:
#
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
#
# with a given n input by console (n>0).


def compute(num):
    if num > 0:
        return (num-1) + 100
    elif num == 0:
        return 1

try:
    print(compute(num=int(input('liczba'))))
except ValueError:
    print('podaj liczbe')