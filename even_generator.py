# Please write a program using generator to print the even numbers between 0 and n
# in comma separated form while n is input by console.


def even_generator(number):
    counter = 0
    while counter <= number:
        if counter % 2 == 0:
            yield counter
        counter += 1


even_numbers = []

for index in even_generator(number=int(input('liczba:\n'))):
    even_numbers.append(str(index))

print(even_numbers)
print(','.join(even_numbers))