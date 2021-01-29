# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

# array = [2, 4, 6, 8, 10]
# for i in array:
#     assert i % 2 == 0


def search(array, target):
    # Definiujmey zmienne, przechowujące zakres, który badamy
    left = 0
    right = len(array)
    index = 0
    # Sprawdzamy czy zakres który jest badany, nie jest pusty

    while left < right:
        # dzielimy listę na 2 zbiory
        index = (left + right) // 2
        print(f'right-{right}')
        print(f'index-{index}')
        print(f'left-{left}')
        print('*******************************************')
        # Jeżeli znaleźliśmy liczbę to kończymy
        # jeżeli lewa strona, jest mniejsza do ją odrzucamy
        # a jeżeli nie, to odrzucamy prawą stronę

        if array[index] == target_number:
            return index
        else:
            if array[index] < target_number:
                left = index + 1

            else:
                right = index
    return -1


A = [1, 3, 4, 5, 7, 9, 11, 15, 16, 17, 19]
target_number = 16

index = search(A, target_number)
print(index)

def sort_array(array):
    i = 0
    while i < len(array):
