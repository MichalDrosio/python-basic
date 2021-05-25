def digit_num(num):
    return (10**int(num))%13

n = 5634

def thirt(n):
    str_n = str(n)
    str_n = str_n[::-1]
    result = 0
    while len(str(result)) != 2:
        print(f'n:{n}|||||||result:{result}')
        for index in range(len(str_n)):
            x = digit_num(index)
            print(x)
            number = int(str_n[index]) * x
            result += number


    return result






# print(thirt(n))

3









