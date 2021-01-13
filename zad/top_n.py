def top_n(array, n):
    array.sort(reverse=True)
    return array[:n]

print(top_n([4,5,2,9,5,2,8,2,8,10], 4))