# Dany jest ciag arytmetyczny:
# An = 10 + 4*n
# Oblicz sume 10 poczatkowych wyrazow tego ciagu
# pierwszy wyraz ciagu
pierwszy = 10 + (4*1)
dziesiaty = 10 + (4*10)
ilosc_wyrazow = 10
suma10 = ((pierwszy+dziesiaty) / 2) * ilosc_wyrazow
print(suma10)

first = 8 * 2**(1-1)
six = 8 * 2**(6-1)
no_num = 6
suma6 = ((first+six) / 2) * no_num
print(suma6)

# Dane jest równanie kwadratowe:
# x**2 + 5x + 4 = 0
a = 1
b = 5
c = 4
suma = -b / a
iloczyn = c / a
print(f'x1+x2= {suma}\nx1x2={iloczyn}')


# Wyznacz środek odcinka o końcach w punktach A=(2,4) B=(-4,6)
A1 = 2
A2 = 4
B1 = -4
B2 = 6
s1 = (A1 + B1) / 2
s2 = (A2 + B2) / 2
print(f'Środek odcinka AB:{s1};{s2}')

# Oblicz odległość dwóch punktów A=(3,2), B=(-1,-1)
a = [3, 2]
b = [-1, -1]
distance = ((b[0]-a[0])**2 + (b[1]-a[1])**2)**(1/2)
print(f'Odległość punktów A i B wynosi {round(distance, 2)}')

