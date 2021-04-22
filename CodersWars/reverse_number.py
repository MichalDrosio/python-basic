def reverse_number(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)


print(reverse_number(123))
print(reverse_number(1000))
print(reverse_number(-123))