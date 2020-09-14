# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n
# in comma separated form while n is input by console.


def divisible_by_5_and_7_generator(number):
    counter = 0
    while counter <= number:
        if counter % 5 == 0 and counter % 7 == 0:
            yield counter
        counter += 1


numbers = []

for index in divisible_by_5_and_7_generator(number=int(input('liczba:\n'))):
    numbers.append(index)

print(numbers)


def num_generator(value):
    for i in range(value+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

values = []
for i in num_generator(value=int(input('liczba:\n'))):
    values.append(str(i))

print(','.join(values))