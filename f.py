def nowa(a):
    try:
        a = int(a)
        w = 5 * a
        return w
    except ValueError:
        print('liczba')


def j(b):
    w = 10*b
    return w



def c(l, l2):
   if type(l) == int and type(l2) == int:
        return l +l2
   else:
       return l * l2


print(c(l=nowa(a=input('l')),l2=j(b=int(input('l2')))))