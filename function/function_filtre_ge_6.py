def filter_ge_6(array):
    array_more_than_6 = []
    for i in array:
        if len(i) >= 6:
            array_more_than_6.append(i)
    return array_more_than_6

print(filter_ge_6(['python', 'java', 'progaraming', 'sql']))