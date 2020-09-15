# Please generate a random float where the value is between 10 and 100 using Python math module
import random

print(random.random()*100)

# Please generate a random float where the value is between 5 and 95 using Python math module.

print(random.random()*100-5)


# Please write a program to output a random even number between 0 and 10
# inclusive using random module and list comprehension.

print(random.choice([i for i in range(11) if i % 2 ==0]))


# Please write a program to output a random number, which is divisible by 5 and 7,
# between 0 and 200 inclusive using random module and list comprehension.

print(random.choice([i for i in range(201) if i % 5 == 0 and i % 7 == 0]))

# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
def five_random_number():
    array = []
    while len(array) != 5:
        number = random.randint(100, 201)
        if number not in array:
            array.append(number)
    return array

print(five_random_number())

print(random.sample(range(100, 201), 5))



# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.


print(random.sample([i for i in range(100, 201) if i % 2 == 0], 5))


# Please write a program to randomly generate a list with 5 numbers,
# which are divisible by 5 and 7 , between 1 and 1000 inclusive.
print(random.sample([i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0], 5))


# Please write a program to randomly print a integer number between 7 and 15 inclusive.
print(random.randrange(7, 16))
print(random.randint(7, 15))


# Please write a program to print the running time of execution of "1+1" for 100 times.
from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())