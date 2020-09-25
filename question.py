# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?


def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j = numheads-i
        print(j)
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns


print(solve(35, 94))