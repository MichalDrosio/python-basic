# Define a function with a generator which can iterate the numbers, which are divisible by 7,
# between a given range 0 and n.


def put_numbers(n):
    counter = 0
    while counter <= n:
        num = counter
        counter += 1
        if num % 7 == 0:
            yield num


def print_result():
    for i in put_numbers(100):
        print(i, end=',')


print_result()

