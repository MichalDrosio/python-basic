def div(array, start, end):
    pivot = array[end]
    low = start
    high = end - 1

    while True:
        while low <= high and array[low] <= pivot:
            low += 1

        while low <= high and array[high] >= pivot:
            high -= 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[end], array[low] = array[low], array[end]
    return low


def quick_sort(array, start, end):
    if start < end:
        pivot = div(array, start, end)
        quick_sort(array, start, pivot-1)
        quick_sort(array, pivot+1, end)
        print(array
              )
array = [2, 4, 1, 0, 9, 6, 5, 8, 7, 3]
print(quick_sort(array, 0, len(array)-1))