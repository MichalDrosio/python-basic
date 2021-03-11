def transpose(array):
    width = len(array[0])
    result = []
    for items in range(width):
        print(items)
        pair = []
        for item in array:
            print(f'item:{item[items]} add to items:{items}')
            pair.append(item[items])
        result.append(pair)
    return result


print(transpose([[1,2,3], [4,5,6]]))