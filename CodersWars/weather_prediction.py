# Let there be k different types of weather, where we denote each type of weather by a positive integer.
# For example, sunny = 0, rainy = 1, ..., cloudy = k.
#
# Task
# Find the probability of having weather j in n days from now given weather i today and conditional
# on some daily weather transition probabilities, a k*k matrix, where i and j are integers less than or equal to k.
#
# Example
# There are two types of weather 0 and 1. Transition probabilities:
#
# [[0.6, 0.4],
#  [0.3, 0.7]]
# The probability of weather 0 tomorrow if weather 0 today: 60%
# The probability of weather 1 tomorrow if weather 0 today: 40%
# The probability of weather 0 tomorrow if weather 1 today: 30%
# The probability of weather 1 tomorrow if weather 1 today: 70%
# The probability of weather 0 two days from now if we start in weather 0 becomes: 60% * 60% + 40% * 30% = 48%.
# Because either we stay in 0 for two days or we go from 0 to 1 and then from 1 to 0.

def weather_prediction(days, today, final, P):
    start, k = P[today], len(P)
    for n in range(days -1):
        start = [sum(start[i] * P[i][j] for i in range(k)) for j in range(k)]
    return start[final]


print(weather_prediction(2, 0, 0, [[0.6, 0.4], [0.3, 0.7]]))