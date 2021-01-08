def remove_duplicates(array):
    return list(set(array))


print(remove_duplicates([1,2,3,2,1,5,6,5,6,7]))


def remove(array):
    result = []
    for i in array:
        if i not in result:
            result.append(i)
    return result


print(remove([1,1,2,2,3,4,5,1,4,5,67]))