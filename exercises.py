# Zadanie 1
#  Narysuj schemat blokowy znajdujący najwyższą liczbę w 10-elementowej tablicy.
array = [1,2,3,4]
print(max(array))


# Zadanie 2
# Narysuj schemat blokowy, który doda wszystkie elementy w 10-elementowej tablicy, a wynik wypisze na ekranie.
array2= [1,2,3,4,5,6,7,8,9,10]
print(sum(array2))

# Zadanie 3
# Narysuj schemat blokowy wypisujący wszystkie pozycje, na których w tablicy A[0, . . . , n-1] znajduje się liczba x.
a = ['q',1,2,'e',3]
for x in a:
    if type(x) == int:
        print(x, end=',')

