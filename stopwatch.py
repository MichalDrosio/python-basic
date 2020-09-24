import time

print('Nacisnij enter aby wystartowac, ponowne wcisniecie spowoduje start nowego okrozenia.')
input()
print('start')
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f'Okrażenie:{lap_num} czas:{lap_time}, czas całkowity:{total_time}', end='')
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print('gotowe')