def insertion_sort(array):
    i = 1
    while i < len(array):
        key = array[i]
        j = i - 1
        print(f'j:{j}, i:{i}, key:{key}')
        while j >= 0 and key < array[j]:
            print(f'{j}>=0 and {key}<{array[j]}')
            print(f'array[j+i]=array[j]|{array[j + 1]} zaminiamy z {array[j]}')
            array[j+1] = array[j]
            print(array)
            j -= 1
        array[j+1] = key
        print(f'array[j+1] = key|{array[j+1]}={key}')
        i += 1
        print(array)
        print('----------')

array = [8, 2, 1, 9, 5]
print(f'start: {array}')

print(insertion_sort(array))