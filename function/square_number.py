def square(a):
    return a**2

s = square
print(s(2))
print(square(2))
print('-----------------')


def print_calculations(function, array):
    for i in array:
        print(function(i))


array = [1,2,3,4]

print_calculations(s, array)


def increase_number(num):
    def increase(num2):
        print(f'num to: {num}\nnum2 tp: {num2}')
        return num + num2
    return increase


i_n = increase_number(10)
print(i_n(7))
print(increase_number(3) (10))




