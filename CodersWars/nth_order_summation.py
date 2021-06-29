# Task
# Consider a series of functions Sm(n) where:
#
# Write a function s which takes two integer arguments m and n and returns the value defined by Sm(n)S_m(n)S
# m
# ​
#  (n).
#
# Inputs
# 0 <= m <= 100
# 1 <= n <= 10**100
import math


def s(m, n):
    num = 1
    for i in range(m):
        num *= (n + i)
    return num // math.factorial(m)




print(s(1 ,49))
