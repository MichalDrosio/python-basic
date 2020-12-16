import uuid

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = self.get_id()

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

    def __repr__(self):
        return f'Book (title={self.title}, author={self.author})'

    def __str__(self):
        return f'Book ID:{self.book_id} | Title:{self.title} | Author:{self.author}'


book = Book('Inferno', 'Dawn Brown')
print(book.__dict__.keys())
print(book.__dict__)
print(book)