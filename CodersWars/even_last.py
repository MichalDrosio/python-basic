def even_last(numbers):
    if numbers == []:
        return 0
    s = 0
    for i in numbers[::2]:
        print(i)
        s += i
    return s * numbers[-1]


# def even_last(numbers):
#     return sum(numbers[::2]) * numbers[-1] if numbers else 0
print(even_last([2,3,4,5]))


