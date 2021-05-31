def test_it(a, b):
    num1 = [int(x) for x in str(a)]
    num2 = [int(x) for x in str(b)]
    return sum(num2) * sum(num1)

print(test_it(200, 200))

