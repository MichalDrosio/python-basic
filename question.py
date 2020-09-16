# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?
# chickens = 0
# rabbits = 0
# heads = 35
# legs = 94
# while heads != 0:
#     legs -= 4
#     rabbits += 1
#     heads -= 1
#     legs -= 2
#     chickens += 1
#     heads -= 1
#
# print(chickens, rabbits)

def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j = numheads-i
        print(j)
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns


print(solve(35, 94))