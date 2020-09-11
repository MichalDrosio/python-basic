# Write a function to compute 5/0 and use try/except to catch the exceptions.


def throws(num):
    return 5/num


try:
    print(throws(0))
except ZeroDivisionError:
    print('Dzielenie przez zero!')

