def transfer_zero(array):
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(0)
    return array


print(transfer_zero([3, 4, 0, 2, 0, 5, 1, 6, 2]))


def transfer_zero(array):
    result = []
    counter = 0
    for i in array:
        if i == 0:
            counter += 1
        else:
            result.append(i)
    result.extend([0] * counter)
    return result
