def flatten(items):
    results = []
    for item in items:
        results.extend(item)
    return results


items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(flatten(items))