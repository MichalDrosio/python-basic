# You found a magic dice which has infinitely many faces showing all the numbers 1,2,3,4,5,....
# By rolling the magic dice infinitely many times, you find out that the probability to get the number n is 1/2^n.
#
# You meet your friend who tells you that he has found another magic dice with infinitely many faces 0,1,2,3,4,5 ..
# But he does not know the probabilities for finding a certain number.
#
# Your friend wants to test his new dice and suggests to play a simple game: Each player rolls his dice three times.
# Each player takes the maximal value of his three results. The player with the larger number wins.
# Your friend rolls his dice three times.
# You are clever and you know that you can, in principle, calculate the probability to win the game. But how?
#
# INPUT: an integer number n>=0
#
# OUTPUT: two integers a and b,
# the numerator and denominator of the probability written as a/b (with the smallest possible b)
# that you will win the game with your three attempts
#
# In Python output as tuple:
#
# return (a, b)
# EXAMPLE: For n=1 the output should be 7 and 8. The probability to roll three times 1 is (1/2)^3=1/8.
# Any other combination wins, and the result is a/b=1-1/8=7/8.


def magicdice(n):
    x = 2 ** (3 * n)
    y = ((2 ** n) - 1) ** 3
    d = x - y
    return (d, x)

print(magicdice(2))