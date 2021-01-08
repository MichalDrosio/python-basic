def map_longest(words_array):
    length = []
    for i in words_array:
        length.append(len(i))
    return max(length)


print(map_longest(['python', 'java', 'sql']))



