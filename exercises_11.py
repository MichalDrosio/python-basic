# Problem: mamy podaną listę liczb. Np. A = [2,1,5,3,6]. Należy posortować ją rosnąco, za pomocą algorytmu bąbelkowego.

def sort(array):
    # nasza pierwsza pętla for
    for n in range(0, len(array) - 1):

        # zmienna, która będzie przechowywać informację czy dokonała się zamiana miejscami. Jest nam ona potrzebna to stwierdzenia czy tablica jest posortowana.
        change = False

        # Druga pętla. Zwróćmy proszę uwagę, że nie zaczyna się ona od 0, a od liczby n, która jest numerem iteracji pierwszej pętli
        for i in range(n, len(array) - 1):

            # Sprawdzamy czy następna liczba na liście jest mniejszy. Jeżeli tak, to znaczy że trzeba zamienić ich kolejność.
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change = True

                # Sprawdzamy czy dokonaliśmy zamiany miejscami chociaż jeden element. Jeżeli nie, to znaczy że lista jest posortowana, a my możemy zakończyć działanie programu
        if change == False:
            return
A = [1,-3,5,1,6,3,2]
sort(A)
print (A)

# Zbadaj czy na liście licz A, znajdują się dwie liczby – a i b, których suma wynosi liczbę L.
#
# Czyli przykładowo, mamy podaną listę A = [1,3,5,2,11,7] . Należy sprawdzić czy suma, którychkolwiek liczb na liście wynosi 9.
# W tym prostym przykładnie już ‘na oko’ widzimy że będą to liczby 2 oraz 7. No dobrze, ale zastanówmy się jak mógłby wyglądać nasz algorytm.


l = 9
x = [1,3,5,2,11,7,8]
for i in x:
    for y in x:
        if i + y == l:
            print(f'{i}+{y}={l}')

