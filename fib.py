

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)


print(fib(num=int(input('liczba'))))


print('------------------------')


def fib_iter1(n):  # definicja funkcji
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą while.
    """
    pwyrazy = (0, 1)  # dwa pierwsze wyrazy ciągu zapisane w tupli
    a, b = pwyrazy  # przypisanie wielokrotne, rozpakowanie tupli
    print(a, end=" ")
    while n > 1:
        print (b, end=" ")
        a, b = b, a + b  # przypisanie wielokrotne
        n -= 1


print(fib_iter1(11))
print('----------------------------------------------')


def fib_iter2(n):
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą for.
    """
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n ):
        a, b = b, a + b

        print("wyraz", i + 2, b)

    print()  # wiersz odstępu
    return b


print(fib_iter2(10))