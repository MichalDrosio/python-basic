def count_str(array):
    result = []
    total = 0
    for i in array:
        if isinstance(i, str):
            result.append(i)
            total += 1
    return total, result

print(count_str(['p', 'python', 1, 3, None]))