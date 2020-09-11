# Define a class named American which has a static method called printNationality.

class American:
    def __init__(self, nationality):
        self.nationality = nationality

    @staticmethod
    def __str__(self):
        return self.nationality


class NewYorker(American):
    def __init__(self, city, nationality):
        super(NewYorker, self).__init__(nationality)
        self.city = city

    def print_person(self):
        print(f'{self.city} is {self.nationality}')


city = NewYorker('NewYork man', 'American')
city.print_person()




