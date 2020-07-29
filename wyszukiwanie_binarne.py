def search(array, target):
    # Definiujmey zmienne, przechowujące zakres, który badamy

    left = 0
    right = len(array)
    index = 0

    # Sprawdzamy czy zakres który jest badany, nie jest pusty

    while left < right:

        # dzielimy listę na 2 zbiory

        index = (left + right) // 2

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


A = [1, 3, 4, 5, 6, 7, 8,12, 14, 16]
target_number = 16
index = search(A, target_number)
print(index)