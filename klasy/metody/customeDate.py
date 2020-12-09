from datetime import datetime


class CustomDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        if self.day < 10:
            if self.month < 10:
                return f'0{self.day}-0{self.month}-{self.year}'
            return f'0{self.day}-{self.month}-{self.year}'
        if self.month < 10:
            return f'{self.day}-0{self.month}-{self.year}'
        return f'{self.day}-{self.month}-{self.year}'

    @classmethod
    def from_text(cls, text):
        day, month, year = text.split('-')
        return cls(int(day), int(month), int(year))

    @classmethod
    def from_text_file(cls, file):
        object_array = []
        with open(file, 'r') as text:
            text_data = text.read().splitlines()
        for date in text_data:
            date_object = cls.from_text(date)
            object_array.append(date_object)
        return object_array

    @staticmethod
    def date_validation(day, month, year):
        try:
            datetime(year, month, day)
        except ValueError:
            raise ValueError('Not valid date!')


