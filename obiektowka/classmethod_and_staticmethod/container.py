import  time


class Container:

    @classmethod
    def show_detail(cls):
        print(f'Running from {cls.__name__} class')

    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())


c = Container()
print(c.get_current_time())