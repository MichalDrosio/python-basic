def merge_sort(array):
    if len(array) > 1:
        mid = int(len(array)//2)
        part_1 = array[:mid]
        part_2 = array[mid:]
        print(f'part1:{part_1}, part2:{part_2}')
        merge_sort(part_1)
        merge_sort(part_2)

        i = 0
        j = 0
        k = 0

        while i < len(part_1) and j < len(part_2):
            if part_1[i] < part_2[j]:
                array[k] = part_1[i]
                i += 1
            else:
                array[k] = part_2[j]
                j += 1
            k += 1

        while i < len(part_1):
            array[k] = part_1[i]
            i += 1
            k += 1

        while j < len(part_2):
            array[k] = part_2[j]
            j += 1
            k += 1

        print(f'po {array}')

array = [1, 3, 2, 6, 4, 10, 9, 7, 8, 11, 0]
print(merge_sort(array))