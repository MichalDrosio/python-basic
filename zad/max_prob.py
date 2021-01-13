def max_prob(array):
    result = []
    for items in array:
        max_val = max(items)
        print(f'max value:{max_val}')
        for item, val in enumerate(items):
            print(f'item_{item}:{val}')
            if val == max_val:
                result.append([val])
    return result

print(max_prob([[0.3, 0.4, 0.3], [0.0, 0.1, 0.9], [0.2, 0.1, 0.7]]))