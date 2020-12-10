class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, value):
        if not isinstance(value, str):
            raise TypeError('The value of the tilt attribute must be of str type')
        self.title = value


book = Book()
print(book.__dict__)
book.author = 'Dan Brown'
book.title = 'Inferno'
print(book.__dict__)

print('-'*100)

book_1 = Book()
book_2 = Book()

book_1.author = 'Tolkien'
book_1.title = 'Hobbit'
book_2.author = 'Tolkien'
book_2.title = 'Lord of ring'
book_2.year_of_publishment = 2000

print(book_1.__dict__)
print(book_2.__dict__)
print('-'*30)
books = [book_1, book_2]
for b in books:
    for attr in b.__dict__:
        print(f'{attr} -> {getattr(b, attr)}')
    print('-'*30)

books_data = [
    {'author': 'Dan Brown', 'title': 'Inferno'},
    {'author': 'Tolkien', 'title': 'Hobbit', 'year_of_publishment': 2000}
]

books_2 = []
for book_data in books_data:
    book_3 = Book()
    for attr, value in book_data.items():
        setattr(book_3, attr, value)
    books_2.append(book_3)

for b in books_2:
    print(b.__dict__)
print('-'*100)

book_4 = Book()
book_4.set_title('Inferno')
print(book_4.title)
book_5 = Book()
book_5.set_title('Inferno')
print(getattr(book_5, 'title'))
print('-'*100)


book_6 = Book()
try:
    book_6.set_title(False)
except TypeError as error:
    print(error)
