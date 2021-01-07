number = 19

if number > 1:
    for i in range(2, number-1):
        if number % i == 0:
            print(f"{number}-isn't prime number")
            break
    else:
        print(f"{number}-prime number")
else:
    print(f"{number}-isn't prime number")