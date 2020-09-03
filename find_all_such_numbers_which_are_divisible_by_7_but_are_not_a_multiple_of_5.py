def find_all_such_numbers_which_are_divisible_by_7_but_are_not_a_multiple_of_5(numbers):
    array = []
    for index in numbers:
        if index % 7 == 0 and index % 5 != 0:
            array.append(index)
    return array

print(find_all_such_numbers_which_are_divisible_by_7_but_are_not_a_multiple_of_5(range(2000, 3200+1)))

