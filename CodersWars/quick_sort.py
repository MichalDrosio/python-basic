import time
from random import randint
z = randint(1,100)
array = [x for x in range(z*20)]
print(array)


def algorytm1(tab):
    min = tab[0]
    max = tab[0]
    t1 = time.perf_counter()

    for i in range(len(tab)):
        if (tab[i] >= max):
            max = tab[i]
        if (tab[i] <= min):
            min = tab[i]
    t2 = time.process_time()

    t3 = t2-t1
    return t3, min, max


def algorytm2(tab):

    min = tab[0]
    max = tab[0]
    t1 = time.perf_counter()

    for i in range(len(tab),2):
        if(tab[i] > tab[i+1]):
            if (tab[i] > max):
                max = tab[i]
            if (tab[i+1] < min):
                min = tab[i+1]
        else:
            if (tab[i+1] > max):
                max = tab[i+1]
            if (tab[i] < min):
                min = tab[i]
    t2 = time.process_time()

    return t2-t1, min, max

print(algorytm1(array))
print(algorytm2(array))