# Define a function that can accept an integer number as input and print the
# "It is an even number" if the number is even, otherwise print "It is an odd number".

def check_even_num(num):
    try:
        num = int(num)
        if num % 2 == 0:
            print(f'{num} is an even number')
        else:
            print(f'{num} is an odd number')
    except ValueError:
        print(f'{num} is not a number')

print(check_even_num(9))