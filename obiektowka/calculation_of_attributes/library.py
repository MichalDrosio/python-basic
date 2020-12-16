class Library:
    def __init__(self, books=None):
        self._book_collection = []

        if books:
            for book in books:
                self.add_book(book)

    @property
    def number_of_books(self):
        return len(self._book_collection)

    def add_book(self, book):
        if book not in self._book_collection:
            self._book_collection.append(book)

    def delete_book(self, book):
        if book in self._book_collection:
            self._book_collection.remove(book)

    def show_book(self):
        print(f'{self._book_collection}')


book1 = Library()
book1.add_book('python')
book1.show_book()
book1.add_book('java')
book1.add_book('python')
book1.show_book()
book1.delete_book('java')
book1.show_book()
book1.add_book(['a', 'd', 'c'])
book1.show_book()