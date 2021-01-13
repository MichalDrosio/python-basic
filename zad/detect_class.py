def detect_class(array):
    results = []

    for items in array:
        max_val = max(items)
        empty = [0] * len(items)
        for item, val in enumerate(items):
            if val == max_val:
                empty[item] = 1
                results.append(empty)
    return results


print(detect_class([[0.3, 0.4, 0.3], [0.0, 0.1, 0.9], [0.2, 0.1, 0.7]]))


