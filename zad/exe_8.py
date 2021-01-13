def arange(start, stop, step=1):
    result = []
    for i in range(start, stop, step):
        result.append(i)
    return result


print(arange(0, 10, 2))