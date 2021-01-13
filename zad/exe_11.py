def fill_value(height, width, value):
    results = [[value] * width for i in range(height)]
    return results


print(fill_value(2, 3, 255))

