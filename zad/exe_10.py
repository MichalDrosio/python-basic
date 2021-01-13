def identity(num):
    result = [[0] * num for i in range(num)]
    for idx, item in enumerate(result):
        item[idx] = 1
    return result


print(identity(4))