import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name ='watek', delay=1, repeating=3):
        super(MyThread, self).__init__()
        self.name = name
        self.delay = delay
        self.repeating = repeating

    def run(self):
        print(f'{self.name} startuje')
        for i in range(self.repeating):
            print(f'{self.name} zatrzymuje sie na {self.delay} sekund')
            time.sleep(self.delay)
            print(f'{self.name} konczy')


print('start')
thread1 = MyThread('Wątek1', 1, 6)
thread2 = MyThread('Wątek2', 2, 3)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('koniec')