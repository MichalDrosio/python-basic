def digit_num(num):
    return (10**int(num))%13


n = 1234567





def thirt(n):
    s = str(n)
    str_n = s[::-1]
    result = 0
    for index in range(len(str_n)):
        x = digit_num(index)
        number = int(str_n[index]) * x
        result += number

    return result



print(thirt(n))



