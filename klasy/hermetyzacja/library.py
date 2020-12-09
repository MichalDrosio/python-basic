class Library:
    def __init__(self, collection=None):
        self._books = []
        if collection:
            for book in collection:
                self.add_book(book)

    @property
    def number_of_books(self):
        return len(self._books)

    def add_book(self, book):
        if book not in self._books:
            self._books.append(book)

    def borrow_book(self, book):
        if book in self._books:
            self._books.remove(book)

    def show_books(self):
        for book in self._books:
            print(book)

c = Library()
c.add_book('a')
c.add_book('e')
c.show_books()