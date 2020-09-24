import time

class Clock:
    def __init__(self, seconds, minutes, hour, mode):
        self.seconds = seconds
        self.minutes = minutes
        self.hour = hour
        self.mode = mode

    def show_clock(self):
        while True:
            print(f'{self.hour}:{self.minutes}:{self.seconds}')
            self.seconds += 1
            time.sleep(1)
            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0
                if self.minutes == 60:
                    self.hour += 1
                    self.minutes = 0
                    if self.mode == 24:
                        if self.hour == 24:
                            self.hour = 0
                        elif self.mode == 12:
                            if self.hour == 12:
                                self.hour = 0
    
    
class Clock_24(Clock):
    def __init__(self, seconds, minutes, hour, mode):
        super(Clock_24, self).__init__(seconds, minutes, hour, mode)


class Clock_12(Clock):
        def __init__(self, seconds, minutes, hour, mode):
            super(Clock_12, self).__init__(seconds, minutes, hour, mode)









