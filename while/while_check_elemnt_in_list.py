numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None

while start <= end:
    print(end)
    mid = int((start + end) / 2)
    print(f'mid:{mid}')
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
            print(f'start:{start}')
        else:
            end = mid - 1
            print(f'end:{end}')

if flag:
    print('ok')
else:
    print('no ok')

