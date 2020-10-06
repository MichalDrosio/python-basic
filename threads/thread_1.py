from threading import Thread
import time

def print_time(name, delay, repeating):
    print(f'{name} wystartowal')
    for i in range(repeating):
        time.sleep(delay)
        print(f'{name} {time.ctime(time.time())}')
    print(f'{name} zakonczyl')


array = []
for i in range(3):
    array.append(Thread(target=print_time, args=(f'Licznik' + str(i+1), i+1, (i+1)**2)))

for x in array:
    x.start()