def diamond(n):
    if n % 2 == 1 and n > 0:
        result = []
        spaces = 0
        for stars in range(n, -1, -2):
            result.append(' ' * spaces + '*' * stars + '\n')
            spaces += 1
        result = result[::-1][:-1] + result
        return ''.join(result)

print(diamond(5))
